import java.util.Scanner;

public class gpa{

	public static void main(String[] args){
	
		String[] name = new String[4];
		String[] grade = new String[4];
		int[] credit = new int[2];
		double calculatedGrade=0.0;
		double result=0.0;
		
		Scanner scan = new Scanner(System.in);
		
		for(int i=0;i<name.length;i++){
			
			System.out.println("Enter Subject name:");

			name[i]=scan.nextLine();
			
			System.out.println("Enter Grade:");
			
			grade[i]=scan.nextLine();

		}
		
		for(int i=0;i<name.length;i++){
			
			if(grade[i].equals("A")){
				calculatedGrade=4.0;
			}
			else if(grade[i].equals("A-")){
				calculatedGrade=3.7;			
			}
			else if(grade[i].equals("B+")){
				calculatedGrade=3.3;			
			}
			else if(grade[i].equals("B")){
				calculatedGrade=3.0;			
			}
			else if(grade[i].equals("B-")){
				calculatedGrade=2.7;			
			}
			else if(grade[i].equals("C+")){
				calculatedGrade=2.3;			
			}
			else if(grade[i].equals("C")){
				calculatedGrade=2.0;			
			}
			else if(grade[i].equals("C-")){
				calculatedGrade=1.7;			
			}
			else if(grade[i].equals("D+")){
				calculatedGrade=1.3;			
			}
			else if(grade[i].equals("D")){
				calculatedGrade=1.0;			
			}			
			else if(grade[i].equals("F")){
				calculatedGrade=0.0;			
			}			
			
			result = result+calculatedGrade;
		}	
	
		for(int i=0;i<name.length;i++){
			System.out.println(" "+name[i]+" "+grade[i]);
		}
		
		System.out.println("GPA:"+result/4);	
	}
}
