describe("Controller", function() {

  var controller
  var homepageView

  beforeEach(function() {
    homepageView = jasmine.createSpyObj('homepageView', ['render'])
    controller = new Controller(homepageView)
  })

  describe("displayHomepage", function() {
    it("hids the results section", function() {
      spyOn($.fn, "hide")
      controller.displayHomepage()
      expect($.fn.hide).toHaveBeenCalled()
    })

    it("renders the homepage view", function() {
      spyOn($.fn, "html")
      controller.displayHomepage()
      expect($.fn.html).toHaveBeenCalledWith(homepageView.render())
    })

    it("listens for form submit", function() {
      spyOn(controller, "_listenForLondonFormSubmit")
      controller.displayHomepage()
      expect(controller._listenForLondonFormSubmit).toHaveBeenCalled()
    })
  })

})
