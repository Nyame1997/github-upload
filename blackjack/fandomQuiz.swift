// Shared Code
// Code written in this file is available on all pages in this Playground Book.

public func fandomQuiz()
{
    show("What’s your name?")
    let name = ask("Name")
    show("Hi, " + name)
    show("What is your favorite fandom?")
    
    let favFandom = ask("Favorite Fandom")
    var fandomTraits: [String] = []
    var letterCounts: [Int] = []
    let questions: [String] = ["Who is the main character?", "Who is the main villain?", "What is the main theme?", "What is the genre?", "Who is your favorite character?", "Who is your favorite villain?"]
    let personalityAnswers: [String] = ["Intelligent", "Adventurous", "Active", "Clever", "Romantic", "Kind"]
    var answerIndex = 0
    
    for question in questions {
        show(question)
        var answer = ask()
        fandomTraits.append(answer)
    }
    
    for trait in fandomTraits {
        letterCounts.append(trait.count)
    }
    
    for count in letterCounts {
        var remainder = count % 5
        answerIndex += remainder
    }
    
    answerIndex = answerIndex % 5
    show(name + " is " + personalityAnswers[answerIndex] + "!")
}
