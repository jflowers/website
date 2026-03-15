---
title: "A Tune-Up for TDD?"
date: "2006-11-20"
draft: false
categories:
  - "Unit Testing"
  - "Testability"
aliases:
  - "/WordPress/?p=96"
  - "/WordPress/index.php?p=96"
params:
  wayback_url: "https://web.archive.org/web/20070212182713/http://jayflowers.com:80/WordPress/?p=96"
  original_url: "http://jayflowers.com:80/WordPress/?p=96"
  archived_from: Wayback Machine

---

## A Tune-Up for TDD?


```batch
If you have read many of my postings to the Yahoo TDD group you may have noticed that I feel that TDD is too difficult to learn. This is of great concern to me. I work in a large company on a large project. I think it should be of great concern to the rest of the Agile community too. It seems to me that TDD presents the greatest risk to successful adoption of an Agile methodology by large projects/organizations.
```

My gut has been pointing me in the general vicinity of testability for just over a year. About a month ago I realized why. The fifth step of TDD, refactor out duplication, is the culprit. The fifth step is geared toward a master not a beginner. Identifying duplication is not as simple as it might sound. Much more than copy and paste duplication is targeted. Behavioral duplication is the real target. Seeing this type of duplication is much more of a right brain activity than a left brain activity. This was the realization. This was the crack in the dam.

So it is important to understand what can happen to a team that is struggling with the fifth step. This is the step that teams seem to have the most trouble with, the first 4 steps are more left brain oriented than right brain. They tend to create tests that are difficult to maintain This can increase the cost of change beyond what the business can support. As a result the unit tests must be dropped. Many times the practice is dropped as well. If the fifth step were not so difficult to learn then tests would be more maintainable and cost of change should be the same if not lower.

It is also important to understand that a what types of activities are controlled by the two hemispheres of the brain. Here is a snippet from [wikipedia](http://en.wikipedia.org/wiki/Right_brain):

> [Reasoning](http://en.wikipedia.org/wiki/Reason) functions such as [language](http://en.wikipedia.org/wiki/Language) are often lateralized to the left hemisphere of the brain. [Dyscalculia](http://en.wikipedia.org/wiki/Dyscalculia) is a [neurological](http://en.wikipedia.org/wiki/Neurology) syndrome associated with damage to the left [temporal](http://en.wikipedia.org/wiki/Temporal_lobe)-[parietal](http://en.wikipedia.org/wiki/Parietal_lobe) junction[[1]](http://en.wikipedia.org/wiki/Right_brain#_note-Levy_1). This syndrome is associated with poor number manipulation, poor mental [arithmetic](http://en.wikipedia.org/wiki/Arithmetic), and an inability to understand or apply mathematical concepts[[1]](http://www.dyscalculia.org/calc.html).
>
> In contrast, visual and [music](http://en.wikipedia.org/wiki/Music) functions such as spatial manipulation, [facial perception](http://en.wikipedia.org/wiki/Face_perception), and artistic ability seem to be lateralized to the right hemisphere.
>
> Other integrative functions such as intuitive or [heuristic](http://en.wikipedia.org/wiki/Heuristic) arithmetic, binaural sound localization, [emotions](http://en.wikipedia.org/wiki/Emotion), etc. seem to be more bilaterally controlled.[[2]](http://en.wikipedia.org/wiki/Right_brain#_note-Dehaene_1)
>
> LEFT BRAIN FUNCTIONS
>
> uses logic, detail oriented, words and language, present and past, math and science, order/pattern perception, knows object name.
>
> RIGHT BRAIN FUNCTIONS
>
> uses feeling, holistically (”big picture”) oriented, symbols and images, present and future, spatial perception, knows object function.

Seeing behavioral duplication is an art, it is a craft. These types of things require much experience to become good at. A good portion of experience in right brain activities includes failure. Left brain activities are much easier to learn and teach. They do not require as much experience to be proficient at.

Refactoring to increase testability is a more left brain activity than a right brain activity. This shift from the right to the left will reduce the risk that the cost of change will increase. On top of that the focus has been adjusted to part of what was increasing the cost in the first place, testability. In practice this would require a change to the test subject to improve testability, run tests expecting success, refactor test to take advantage of the increased testability, and finally run tests expecting success.

To sum up the advantages that I see to changing the fifth step to Refactor to Increase Testability:

- Easier to learn and teach.

- Shorter time spent in the [improvement ravine](http://martinfowler.com/bliki/ImprovementRavine.html).

- Less productivity lost to learning something new.

- Less cost of teaching something new.

- Less risk to successful adoption of TDD.

- Less chance of difficult to maintain tests being produced.
- Improved testability of product.

- All the benefits that come with [testability](http://jayflowers.com/WordPress/?p=77).

- Less resistance to something easier to understand and explain.
- There are metrics for testability.

I am hoping to give this a test on the project that I am currently on. The group is not all on the same page about how to produce unit tests. That is as far as the commitment has gone. It has taken us a long time to get to that agreement. Points being that this is all armchair reasoning and I hope to put it to the test. I did feel it worth sharing with the community even if it is unproven. You might feel it is worth a shot and benefit from it.

I have explained testability in other postings but I think it bears repeating here.

There are three aspects of testability; Observability, Controllability, and Understandability. To test something you must be able to observe or sense that it did what it was supposed to do. To test something you must be able to control or manipulate it. Control is needed at the very least to instigate it to do the thing that you desire to test. In the case of unit tests and some other testing the control will be used to isolate the test subject. To test something you must be able to know: What needs to be controlled and observed. How to control what needs to be controlled. Lastly what the out come should be.

In general I have found that it pays to have less to work with in a test. That is to say that when there are very few types and members involved in a test it will be easier to understand. It is easier to observe and control less than more. When you can’t have less it pays to have a test double.

It seems there are two general fulcrums that you have to control testability. They are decreasing the surface area and type population or introducing test doubles. As well, they help in increasing the effectiveness of unit tests by eliminating failure points other than the test subject.

Those last few paragraphs are the wisdom that I have collected. Sometimes as a newbie it is hard to see how to apply store bought wisdom. I posted a [list of questions](http://jayflowers.com/WordPress/?p=64) last summer that can easily direct you to areas where action could be taken to improve testability.

Besides getting you to truly understand testability one of the main points that I am trying to make here is you already have a good understanding of what testability is. I doubt that I told you anything new. At most you may have thought ahh that is what I knew all a long but have never verbalized. Because you already have a good understanding of what testability is you will be less resistant to actually performing the step of refactoring to increase testability. My experience with refactoring to remove duplication has proven to be that of resistance. Many people do not truly understand what it is nor do they see how it ties back into and supports/enables the process to continue. It is far easier to see how refactor to increase testability ties back in and supports the process to continue.

P.S. Once you have mastered testability I would add in duplication.
