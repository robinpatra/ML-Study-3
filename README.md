# k-days Machine Learning Journey

[![Netlify Status](https://api.netlify.com/api/v1/badges/a70311c1-33ec-4c4a-afa6-93f453016ea5/deploy-status)](https://app.netlify.com/sites/ml-journey/deploys)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Learning Resources](#learning-resources)
- [Quick Start](#quick-start)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Learning Resources

- A Cloud Guru (Paid)
  - Course
    - [Introduction to Machine Learning](https://acloud.guru/learn/intro-machine-learning)
  - ACG Projects
    - [#107 - Does Twitter Hate Cats?](https://acloud.guru/series/acg-projects/view/107)
    - [#208 - Angry Ferret Detector: Use and Publish AWS Marketplace Machine Learning Resources for Fun and Profit!](https://acloud.guru/series/acg-projects/view/208)
    - [#301 The Smile Detector](https://acloud.guru/series/acg-projects/view/301)
  - Series
    - [DeepRacer: The Fast and the Curious](https://acloud.guru/series/deepracer)
- Coursera
  - [Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning) (**Free**)
- Data Camp (Paid. **Free 3 months with GitHub Education Pack**)
  - [Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science)
- Khan Academy (**Free**)
  - [6th grade Data and statistics](https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics)
  - [High school statistics](https://www.khanacademy.org/math/probability)
  - [Statistics and probability](https://www.khanacademy.org/math/statistics-probability)

## Quick Start

Clean clone:

```bash
git clone --recurse-submodules -j8 git@github.com:siutsin/k_days_machine_learning_journey.git
```

(Optional) Update submodule:

```bash
git submodule update --init --recursive
```

Install Hugo via [homebrew](https://brew.sh/) (macOS). Other OS refer to the [Official Doc](https://gohugo.io/getting-started/installing/).

```bash
brew install hugo
```

Start Hugo local server

```bash
hugo server --disableFastRender --buildDrafts
# Server runs at http://localhost:1313/
```

## License

The content of this project is licensed under the [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).

The underlying source code is licensed under the [MIT license](LICENSE.md).
