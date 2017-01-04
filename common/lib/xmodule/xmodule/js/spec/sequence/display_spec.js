/* globals Sequence */
(function() {
    'use strict';

    describe('Sequence', function() {
        var keydownHandler,
            keys = {
                ENTER: 13,
                LEFT: 37,
                UP: 38,
                RIGHT: 39,
                DOWN: 40
            };
        beforeEach(function() {
            loadFixtures('sequence.html');
            window.XBlock = jasmine.createSpyObj('XBlock', ['initializeBlocks']);
        });

        afterEach(function() {
            delete window.XBlock;
        });

        keydownHandler = function(key) {
            var event = document.createEvent('Event');
            event.keyCode = key;
            event.initEvent('keydown', false, false);
            document.dispatchEvent(event);
        };

        describe('Navbar', function() {
            it('works with keyboard navigation LEFT and ENTER', function() {
                this.sequence = new Sequence($('.xblock-student_view-sequential'));
                this.sequence.$('.nav-item[data-index=0]').focus();
                keydownHandler(keys.LEFT);
                keydownHandler(keys.ENTER);

                expect(this.sequence.$('.nav-item[data-index=1]')).toHaveAttr({
                    'aria-expanded': 'false',
                    'aria-selected': 'false',
                    tabindex: '-1'
                });
                expect(this.sequence.$('.nav-item[data-index=0]')).toHaveAttr({
                    'aria-expanded': 'true',
                    'aria-selected': 'true',
                    tabindex: '0'
                });
            });

            it('works with keyboard navigation UP and ENTER', function() {
                this.sequence = new Sequence($('.xblock-student_view-sequential'));
                this.sequence.$('.nav-item[data-index=0]').focus();
                keydownHandler(keys.UP);
                keydownHandler(keys.ENTER);

                expect(this.sequence.$('.nav-item[data-index=1]')).toHaveAttr({
                    'aria-expanded': 'false',
                    'aria-selected': 'false',
                    tabindex: '-1'
                });
                expect(this.sequence.$('.nav-item[data-index=0]')).toHaveAttr({
                    'aria-expanded': 'true',
                    'aria-selected': 'true',
                    tabindex: '0'
                });
            });

            it('works with keyboard navigation RIGHT and ENTER', function() {
                this.sequence = new Sequence($('.xblock-student_view-sequential'));
                this.sequence.$('.nav-item[data-index=0]').focus();
                keydownHandler(keys.RIGHT);
                keydownHandler(keys.ENTER);

                expect(this.sequence.$('.nav-item[data-index=0]')).toHaveAttr({
                    'aria-expanded': 'false',
                    'aria-selected': 'false',
                    tabindex: '-1'
                });
                expect(this.sequence.$('.nav-item[data-index=1]')).toHaveAttr({
                    'aria-expanded': 'true',
                    'aria-selected': 'true',
                    tabindex: '0'
                });
            });

            it('works with keyboard navigation DOWN and ENTER', function() {
                this.sequence = new Sequence($('.xblock-student_view-sequential'));
                this.sequence.$('.nav-item[data-index=0]').focus();
                keydownHandler(keys.DOWN);
                keydownHandler(keys.ENTER);

                expect(this.sequence.$('.nav-item[data-index=0]')).toHaveAttr({
                    'aria-expanded': 'false',
                    'aria-selected': 'false',
                    tabindex: '-1'
                });
                expect(this.sequence.$('.nav-item[data-index=1]')).toHaveAttr({
                    'aria-expanded': 'true',
                    'aria-selected': 'true',
                    tabindex: '0'
                });
            });
        });
    });
}).call(this);
