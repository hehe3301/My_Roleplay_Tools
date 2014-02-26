public class Player {
	private String name;
	private int age;
	private String gender;
	private String orentation;
	private Boolean isAwake;
	private Boolean isPartyMember;

	public Player(String name, int age,String gender,Boolean isPartyMember) {
		this.name = name;
		this.age = 18;
		this.gender = "Male";
		this.orentation = "Heterosexual";
		this.isAwake = true;
		this.isPartyMember = false;
	}
	public String toString(){
		return this.name + " " + this.age + " " +gender;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public String getOrentation() {
		return orentation;
	}

	public void setOrentation(String orentation) {
		this.orentation = orentation;
	}

	public Boolean getIsAwake() {
		return isAwake;
	}

	public void setIsAwake(Boolean isAwake) {
		this.isAwake = isAwake;
	}

	public Boolean getIsPartyMember() {
		return isPartyMember;
	}

	public void setIsPartyMember(Boolean isPartyMember) {
		this.isPartyMember = isPartyMember;
	}
	
	public String getName(){
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

}
