/**
 * The MoveXblockModal to move XBlocks in course.
 */
define(['jquery', 'backbone', 'underscore', 'gettext', 'js/views/baseview', 'js/views/modals/base_modal'
], function(
    $, Backbone, _, gettext, BaseView, BaseModal
) {
    'use strict';

    var MoveXblockModal = BaseModal.extend({
        events: _.extend({}, BaseModal.prototype.events, {
            'click .action-move': 'moveXBlock'
        }),

        options: $.extend({}, BaseModal.prototype.options, {
            modalName: 'move-xblock',
            modalSize: 'med',
            viewSpecificClasses: 'confirm',
            title: gettext('Move'),
            primaryActionButtonType: 'move',
            primaryActionButtonTitle: gettext('Move')
        }),

        initialize: function() {
            BaseModal.prototype.initialize.call(this);
            this.template = this.loadTemplate('move-xblock-modal');
            this.sourceXBlockInfo = this.options.sourceXBlockInfo;
            this.XBlockUrlRoot = this.options.sourceXBlockInfo;
            this.options.title = this.getTitle();
        },

        getContentHtml: function() {
            return this.template(this.getContext());
        },

        moveXBlock: function(event) {
        },

        getContext: function() {
            return {
                displayName: '"' + this.sourceXBlockInfo.get('display_name') + '"'
            };
        }
    });

    return MoveXblockModal;
});
