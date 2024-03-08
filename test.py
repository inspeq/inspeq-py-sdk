from inspeq.client import Evaluator
import time


API_KEY = "your_sdk_api_key"
inspeq_instance = Evaluator(sdk_api_key=API_KEY)

data_objects=[
    
  {
    "llm_input_query": "What are the key principles of object-oriented programming?",
    "llm_input_context": "Object-oriented programming (OOP) is a programming paradigm based on the concept of 'objects', which can contain data, in the form of fields, and code, in the form of procedures...",
    "llm_output": "Object-oriented programming (OOP) revolves around four key principles: encapsulation, inheritance, polymorphism, and abstraction. Encapsulation refers to the bundling of data and methods that operate on the data into a single unit or class. Inheritance enables the creation of new classes based on existing ones, allowing for code reuse and hierarchical classification. Polymorphism allows objects to be treated as instances of their parent class, enabling flexibility and modularity in code design. Abstraction involves simplifying complex systems by focusing on essential properties and hiding implementation details."
  },
  {
    "llm_input_query": "Explain the concept of recursion in computer science.",
    "llm_input_context": "Recursion is a fundamental concept in computer science and mathematics...",
    "llm_output": "Recursion is a programming technique where a function calls itself in order to solve a problem. It is based on the principle of breaking down a problem into smaller, more manageable subproblems that are similar in structure to the original problem. In each recursive call, the function operates on a smaller subset of the problem until a base case is reached, at which point the recursion stops. Recursion is often used to solve problems that can be defined in terms of smaller instances of the same problem, such as traversing tree structures, sorting algorithms, and mathematical computations like factorials and Fibonacci sequences."
  },
  {
    "llm_input_query": "What are the advantages of using a relational database management system (RDBMS)?",
    "llm_input_context": "Relational database management systems (RDBMS) are a type of database management system that stores data in a structured format, using rows and columns...",
    "llm_output": "Relational database management systems (RDBMS) offer several advantages, including data integrity, scalability, concurrency control, and ease of querying. With RDBMS, data integrity is maintained through the use of constraints, such as primary keys, foreign keys, and unique constraints, which enforce rules for data consistency and accuracy. RDBMS are also highly scalable, allowing for the storage and retrieval of large volumes of data across multiple tables and databases. Concurrency control mechanisms ensure that multiple users can access and modify the database simultaneously without conflicting with each other. Additionally, RDBMS provide a standardized query language, such as SQL (Structured Query Language), which enables users to retrieve and manipulate data using simple and powerful commands."
  },
  {
    "llm_input_query": "Explain the concept of machine learning and its applications.",
    "llm_input_context": "Machine learning is a branch of artificial intelligence (AI) that focuses on the development of algorithms and statistical models...",
    "llm_output": "Machine learning is a branch of artificial intelligence (AI) that focuses on the development of algorithms and statistical models that enable computers to learn from and make predictions or decisions based on data. It encompasses various techniques, including supervised learning, unsupervised learning, and reinforcement learning. Supervised learning involves training a model on labeled data, where the desired output is known, to make predictions on new data. Unsupervised learning involves training a model on unlabeled data to discover hidden patterns or structures within the data. Reinforcement learning involves training a model to make sequential decisions by interacting with an environment and receiving feedback in the form of rewards or penalties. Machine learning has numerous applications across various domains, including image and speech recognition, natural language processing, recommendation systems, autonomous vehicles, and healthcare."
  },
  {
    "llm_input_query": "What are the principles of good software design?",
    "llm_input_context": "Good software design is essential for creating maintainable, scalable, and efficient software systems...",
    "llm_output": "Good software design is characterized by several key principles, including modularity, abstraction, encapsulation, and reusability. Modularity involves breaking down a system into smaller, independent modules or components that can be developed, tested, and maintained separately. Abstraction involves hiding unnecessary details and exposing only essential features or functionalities to simplify complexity and improve clarity. Encapsulation involves bundling data and methods that operate on the data into a single unit or class to control access and enforce data integrity. Reusability involves designing components or modules that can be reused across different parts of the system or in other projects, reducing duplication of effort and improving productivity."
  },
  {
    "llm_input_query": "What are the main characteristics of functional programming languages?",
    "llm_input_context": "Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data...",
    "llm_output": "Functional programming languages are characterized by several key features, including first-class functions, immutability, higher-order functions, and declarative syntax. First-class functions treat functions as first-class citizens, allowing them to be assigned to variables, passed as arguments to other functions, and returned as results from other functions. Immutability refers to the practice of avoiding mutable state, where once a value is assigned, it cannot be changed, which reduces the risk of side effects and makes code easier to reason about. Higher-order functions enable the composition of functions by taking other functions as arguments or returning functions as results, providing flexibility and modularity in code design. Declarative syntax focuses on describing what should be done rather than how it should be done, emphasizing the use of expressions and transformations to manipulate data."
  },
  {
    "llm_input_query": "What are the fundamental concepts of cybersecurity?",
    "llm_input_context": "Cybersecurity is the practice of protecting computer systems, networks, and data from unauthorized access, attacks, and damage...",
    "llm_output": "Cybersecurity encompasses several fundamental concepts, including confidentiality, integrity, availability, authentication, and non-repudiation. Confidentiality refers to the protection of sensitive information from unauthorized access or disclosure, ensuring that only authorized individuals can access the data. Integrity involves maintaining the accuracy and consistency of data throughout its lifecycle, preventing unauthorized modifications or alterations. Availability ensures that systems and data are accessible and usable when needed, minimizing downtime and disruptions to operations. Authentication verifies the identity of users or entities attempting to access a system or resource, typically through credentials such as passwords, biometrics, or cryptographic keys. Non-repudiation provides proof of the origin or delivery of data and prevents parties from denying their involvement in a transaction or communication."
  },
  {
  "llm_input_query": "What are the effects of climate change on global ecosystems?",
  "llm_input_context": "Climate change refers to long-term changes in temperature, precipitation, and other atmospheric conditions on Earth. It is primarily caused by human activities such as burning fossil fuels, deforestation, and industrial processes...",
  "llm_output": "Climate change has significant effects on global ecosystems, leading to biodiversity loss, habitat destruction, and altered ecosystems. Rising temperatures disrupt the balance of ecosystems, affecting species distributions, migration patterns, and reproductive cycles. Changes in precipitation patterns result in droughts, floods, and wildfires, further impacting ecosystems and species survival. Ocean acidification, caused by increased carbon dioxide absorption, affects marine ecosystems, leading to coral bleaching, declining fish populations, and loss of habitat for marine organisms. Melting ice caps and glaciers threaten polar ecosystems, affecting polar bears, penguins, and other species dependent on ice for survival. In terrestrial ecosystems, climate change alters vegetation patterns, leading to changes in food availability and habitat suitability for wildlife. Overall, climate change poses a significant threat to global ecosystems and biodiversity, requiring urgent mitigation measures to reduce its impact."
},
{
  "llm_input_query": "What are the advantages and disadvantages of renewable energy sources?",
  "llm_input_context": "Renewable energy sources such as solar, wind, hydroelectric, and biomass offer alternatives to traditional fossil fuels for electricity generation. They are considered environmentally friendly and sustainable...",
  "llm_output": "Renewable energy sources offer several advantages, including reduced greenhouse gas emissions, energy independence, and job creation. Solar energy harnesses sunlight using photovoltaic cells or solar thermal systems, providing a clean and abundant source of electricity. Wind energy utilizes wind turbines to generate electricity, offering a renewable and cost-effective solution for power generation. Hydroelectric power harnesses the energy of flowing water to produce electricity, providing a reliable and renewable energy source. Biomass energy utilizes organic materials such as wood, crops, and organic waste to produce heat or electricity, offering a carbon-neutral alternative to fossil fuels. However, renewable energy sources also have some disadvantages, including intermittent energy production, high initial costs, and environmental impacts. Solar and wind energy production can be variable and dependent on weather conditions, requiring backup power sources or energy storage systems. The initial investment in renewable energy infrastructure can be expensive, although costs are decreasing over time. Additionally, large-scale deployment of renewable energy technologies may have environmental impacts such as habitat disruption and land use changes. Despite these challenges, the transition to renewable energy is essential for mitigating climate change and reducing dependence on finite fossil fuel resources."
},
{
  "llm_input_query": "What are the main causes of air pollution in urban areas?",
  "llm_input_context": "Air pollution in urban areas is a pressing environmental issue that affects public health and the quality of life. It is caused by a variety of factors, including industrial activities, vehicle emissions, construction activities, and residential heating...",
  "llm_output": "Air pollution in urban areas is primarily caused by emissions from vehicles, industrial activities, and combustion processes. Vehicle emissions, including exhaust gases and particulate matter, contribute significantly to urban air pollution, especially in areas with heavy traffic congestion. Industrial activities such as manufacturing, power generation, and waste incineration release pollutants such as sulfur dioxide, nitrogen oxides, and volatile organic compounds into the atmosphere, affecting air quality in surrounding areas. Construction activities, including demolition, excavation, and building materials production, generate dust and particulate matter that can contribute to local air pollution. Residential heating using fossil fuels such as coal, wood, and oil releases pollutants such as carbon monoxide and fine particulate matter into the air, especially during the winter months. Other sources of urban air pollution include agricultural activities, wildfires, and natural sources such as pollen and mold spores. Overall, addressing the main causes of air pollution in urban areas requires implementing measures to reduce emissions from vehicles, industry, and other sources, as well as promoting clean energy technologies and sustainable urban planning practices."
}



]
a=time.time()
for i, data_object in enumerate(data_objects, start=1):
    input_data = {
        "llm_input_query": data_object["llm_input_query"],
        "llm_input_context": data_object["llm_input_context"],
        "llm_output": data_object["llm_output"],
    }
    print("Factual Consistency:", inspeq_instance.factual_consistency(input_data))
    print("Answer Relevance:", inspeq_instance.answer_relevance(input_data))
    print("Response Tone:", inspeq_instance.response_tone(input_data))
    print("Grammatical Correctness:", inspeq_instance.grammatical_correctness(input_data))
    print("Fluency:", inspeq_instance.fluency(input_data))
    print("Do Not Use Keywords:", inspeq_instance.do_not_use_keywords(input_data))
    print("Word Limit Test:", inspeq_instance.word_limit_test(input_data))
    print("Conceptual Similarity:", inspeq_instance.conceptual_similarity(input_data))
    print("Coherence:", inspeq_instance.coherence(input_data))
    print("Readability:", inspeq_instance.readability(input_data))
    print("Clarity:", inspeq_instance.clarity(input_data))
    print("get all metrics:", inspeq_instance.get_all_metrics(input_data))


# input_data = {
#     "llm_input_query": "What are the fundamental concepts of cybersecurity?",
#     "llm_input_context": "Cybersecurity is the practice of protecting computer systems, networks, and data from unauthorized access, attacks, and damage...",
#     "llm_output": "Cybersecurity encompasses several fundamental concepts, including confidentiality, integrity, availability, authentication, and non-repudiation. Confidentiality refers to the protection of sensitive information from unauthorized access or disclosure, ensuring that only authorized individuals can access the data. Integrity involves maintaining the accuracy and consistency of data throughout its lifecycle, preventing unauthorized modifications or alterations. Availability ensures that systems and data are accessible and usable when needed, minimizing downtime and disruptions to operations. Authentication verifies the identity of users or entities attempting to access a system or resource, typically through credentials such as passwords, biometrics, or cryptographic keys. Non-repudiation provides proof of the origin or delivery of data and prevents parties from denying their involvement in a transaction or communication."     }

b=time.time()
print("time to execute :",b-a)

