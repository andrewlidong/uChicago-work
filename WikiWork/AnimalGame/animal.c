//Andrew Dong
//animal.c 

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <libxml/tree.h>
#include <libxml/parser.h>
#include <libxml/xpath.h>
#include <libxml/xpathInternals.h>

typedef struct tree_entry{
        char *text; //animal name or question
        struct tree_entry *yes; //if yes, continue to this entry
        struct tree_entry *no; //if no, continue to this entry
} tree_entry;

char *new_text(char *text){ //alloc new memory for string and copy over old string
        char *newtext = (char *) malloc(sizeof(char) * strlen(text) + 1);
        assert(newtext != NULL);
        int i;
        for (i = 0; i<(strlen(text)); i++){ //copy word to new loc
                newtext[i] = text[i];
        }
        newtext[i] = '\0';
        return newtext;
}

char *cat_text(char *one, char *two){ //alloc new memory for string and copy over old string
        char *newtext = (char *) malloc(strlen(one) + strlen(two) + 1);
        assert(newtext != NULL);
        strcpy (newtext, one);
        strcat (newtext, two);
        return newtext;
}

tree_entry *new_entry(char *text, tree_entry *yes, tree_entry *no){ //create new tree entry
        tree_entry *result = (tree_entry *) malloc(sizeof(tree_entry));
        assert(result != NULL);

        result->text = new_text(text);
        result->yes = yes;
        result->no = no;

        return result;
}

void free_entry(tree_entry *e) {
        if (e != NULL){
                if (e->yes != NULL){
                        free_entry(e->yes);
                }
                if (e->no != NULL){
                        free_entry(e->no);
                }
                free ((void *) e->text);
                free ((void *) e);
        }
}

int ask(){ //takes input for (y/n) prompt and returns 1 if 'y'
        char yn[128];

        fgets(yn,127,stdin);
        return(yn[0] == 'y');
}

char *input(){ //returns input without newline
        static char result[128];

        fgets(result,127,stdin);
        if (result[strlen(result) - 1] == '\n')
                result[strlen(result) - 1] = '\0';

        return result;
}
int exists(const char *fname) { //check if xml file exsits
    FILE *file;
    if ((file = fopen(fname, "r")))
    {
        fclose(file);
        return 1;
    }
    return 0;
}

void entryToXML(tree_entry *e, xmlNode *a_node){ //adds child to xml tree
        xmlNewChild(a_node, NULL, BAD_CAST "text", BAD_CAST new_text(e->text));
        xmlNode *yes = xmlNewChild(a_node, NULL, BAD_CAST "yes", BAD_CAST "");
        xmlNode *no = xmlNewChild(a_node, NULL, BAD_CAST "no", BAD_CAST "");

        if (e->yes != NULL){
                entryToXML(e->yes, yes);
        } else {
                xmlNewChild(yes, NULL, BAD_CAST "text", NULL);
        }

        if (e->no != NULL){
                entryToXML(e->no, no);
        } else {
                xmlNewChild(no, NULL, BAD_CAST "text", NULL);

        }
}

tree_entry *XMLtoEntry(xmlXPathContextPtr context, char *expr){ //reads xml tree to entry node tree
        char *addtext = cat_text(expr,"/text");
    xmlXPathObjectPtr result = xmlXPathEvalExpression((xmlChar *) addtext,context);
    free ((void *) addtext);

    assert(result != NULL);
    assert(result->type == XPATH_NODESET);

    xmlNodeSetPtr nodeset = result->nodesetval;
    xmlBufferPtr buffer = xmlBufferCreate();
    xmlNodePtr contentNode = nodeset->nodeTab[0];
    assert(xmlNodeBufGetContent(buffer,contentNode) == 0);
    xmlXPathFreeObject(result);

    if (!strcmp((char *)buffer->content,"")){
                return NULL;
    } else {
                char *addyes = cat_text(expr,"/yes");
                char *addno = cat_text(expr,"/no");
                return new_entry((char *) buffer->content, XMLtoEntry(context, addyes), XMLtoEntry(context, addno));
    }
}

int main(int argc, char **argv){
        xmlDoc *doc = NULL;
        xmlNode *root_node = NULL;
        tree_entry *start = NULL;


        if (!exists("animal.xml")){ //if file doesn't exist
                start = new_entry("Is it a mammal?", new_entry("cat",NULL,NULL), new_entry("alligator",NULL,NULL)); //original question and answers
        } else {
                //read in xml file
                doc = xmlReadFile("animal.xml", NULL, 0);

            if (doc == NULL) {
                printf("error: could not parse file %s\n", argv[1]);
            }

            root_node = xmlDocGetRootElement(doc);

            xmlXPathContextPtr context = xmlXPathNewContext(doc);
            assert(context != NULL);

            start = XMLtoEntry(context, "/root");


            xmlXPathFreeContext(context);  
            xmlFreeDoc(doc);
            xmlCleanupParser();
            xmlMemoryDump();
        }




        printf("Welcome to the Animal Game!\n\n");

        do { //loops while player wants to play again
                tree_entry *current = start; //point to current entry
                while(current->yes != NULL && current->no != NULL){ //current entry is a question
                        printf("%s (y/n): ", current->text); //print question
                        if(ask()){ //answers question with yes
                                current = current->yes; //point to next entry
                        }else { //with no
                                current = current->no; //point to next entry
                        }
                } 

                //current entry is an animal
                printf("Is your animal a %s? (y/n): ", current->text); //print question
                if(ask()){ //animal guess is correct
                        printf("I win!\n");
                }else { //is wrong
                        current->no = new_entry(current->text, NULL, NULL); //change no entry
                        printf("I lose\n");
                        printf("What was your animal? ");
                        char *new_animal = input(); //get input
                        current->yes = new_entry(new_animal,NULL,NULL); //change yes entry


                        printf("Please state a question that is true of a %s but false of a %s: ",new_animal,current->text);
                        char *new_question = input(); //get input
                        current->text = new_text(new_question); //change text of entry
                }

        printf("Would you like to play again? (y/n): ");
    } while(ask()); //get input


    //Write to xml file
    doc = xmlNewDoc(BAD_CAST "1.0");
    root_node = xmlNewNode(NULL, BAD_CAST "root");
    xmlDocSetRootElement(doc, root_node);
    entryToXML(start, root_node);


    xmlSaveFormatFileEnc("animal.xml", doc, "UTF-8", 1);
    xmlFreeDoc(doc);
    xmlCleanupParser();
    xmlMemoryDump();
    free_entry(start); //free allocated memory
}
