# coding: utf-8

import pprint
import re

import six





class VideoTypeRef:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'video_type': 'str',
        'title': 'str',
        'description': 'str',
        'category_id': 'int',
        'tags': 'str',
        'auto_publish': 'int',
        'template_group_name': 'str',
        'auto_encrypt': 'int',
        'auto_preheat': 'int',
        'thumbnail': 'Thumbnail',
        'review': 'Review',
        'workflow_name': 'str'
    }

    attribute_map = {
        'video_type': 'video_type',
        'title': 'title',
        'description': 'description',
        'category_id': 'category_id',
        'tags': 'tags',
        'auto_publish': 'auto_publish',
        'template_group_name': 'template_group_name',
        'auto_encrypt': 'auto_encrypt',
        'auto_preheat': 'auto_preheat',
        'thumbnail': 'thumbnail',
        'review': 'review',
        'workflow_name': 'workflow_name'
    }

    def __init__(self, video_type=None, title=None, description=None, category_id=None, tags=None, auto_publish=None, template_group_name=None, auto_encrypt=None, auto_preheat=None, thumbnail=None, review=None, workflow_name=None):
        """VideoTypeRef - a model defined in huaweicloud sdk"""
        
        

        self._video_type = None
        self._title = None
        self._description = None
        self._category_id = None
        self._tags = None
        self._auto_publish = None
        self._template_group_name = None
        self._auto_encrypt = None
        self._auto_preheat = None
        self._thumbnail = None
        self._review = None
        self._workflow_name = None
        self.discriminator = None

        if video_type is not None:
            self.video_type = video_type
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
        if tags is not None:
            self.tags = tags
        if auto_publish is not None:
            self.auto_publish = auto_publish
        if template_group_name is not None:
            self.template_group_name = template_group_name
        if auto_encrypt is not None:
            self.auto_encrypt = auto_encrypt
        if auto_preheat is not None:
            self.auto_preheat = auto_preheat
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if review is not None:
            self.review = review
        if workflow_name is not None:
            self.workflow_name = workflow_name

    @property
    def video_type(self):
        """Gets the video_type of this VideoTypeRef.

        视频类型<br/> 

        :return: The video_type of this VideoTypeRef.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this VideoTypeRef.

        视频类型<br/> 

        :param video_type: The video_type of this VideoTypeRef.
        :type: str
        """
        self._video_type = video_type

    @property
    def title(self):
        """Gets the title of this VideoTypeRef.

        媒资标题</br> 

        :return: The title of this VideoTypeRef.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this VideoTypeRef.

        媒资标题</br> 

        :param title: The title of this VideoTypeRef.
        :type: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this VideoTypeRef.

        视频描述<br/> 

        :return: The description of this VideoTypeRef.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VideoTypeRef.

        视频描述<br/> 

        :param description: The description of this VideoTypeRef.
        :type: str
        """
        self._description = description

    @property
    def category_id(self):
        """Gets the category_id of this VideoTypeRef.

        媒资分类id<br/> 

        :return: The category_id of this VideoTypeRef.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this VideoTypeRef.

        媒资分类id<br/> 

        :param category_id: The category_id of this VideoTypeRef.
        :type: int
        """
        self._category_id = category_id

    @property
    def tags(self):
        """Gets the tags of this VideoTypeRef.

        视频标签<br/> 

        :return: The tags of this VideoTypeRef.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VideoTypeRef.

        视频标签<br/> 

        :param tags: The tags of this VideoTypeRef.
        :type: str
        """
        self._tags = tags

    @property
    def auto_publish(self):
        """Gets the auto_publish of this VideoTypeRef.

        是否自动发布<br/> 

        :return: The auto_publish of this VideoTypeRef.
        :rtype: int
        """
        return self._auto_publish

    @auto_publish.setter
    def auto_publish(self, auto_publish):
        """Sets the auto_publish of this VideoTypeRef.

        是否自动发布<br/> 

        :param auto_publish: The auto_publish of this VideoTypeRef.
        :type: int
        """
        self._auto_publish = auto_publish

    @property
    def template_group_name(self):
        """Gets the template_group_name of this VideoTypeRef.

        转码模板组名称<br/> 

        :return: The template_group_name of this VideoTypeRef.
        :rtype: str
        """
        return self._template_group_name

    @template_group_name.setter
    def template_group_name(self, template_group_name):
        """Sets the template_group_name of this VideoTypeRef.

        转码模板组名称<br/> 

        :param template_group_name: The template_group_name of this VideoTypeRef.
        :type: str
        """
        self._template_group_name = template_group_name

    @property
    def auto_encrypt(self):
        """Gets the auto_encrypt of this VideoTypeRef.

        是否自动加密，取值[0，1]，0表示需要不加密；1表示需要加密。加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出必须要为HLS 

        :return: The auto_encrypt of this VideoTypeRef.
        :rtype: int
        """
        return self._auto_encrypt

    @auto_encrypt.setter
    def auto_encrypt(self, auto_encrypt):
        """Sets the auto_encrypt of this VideoTypeRef.

        是否自动加密，取值[0，1]，0表示需要不加密；1表示需要加密。加密与转码必须要一起进行，当需要加密时，转码参数不能为空，且转码输出必须要为HLS 

        :param auto_encrypt: The auto_encrypt of this VideoTypeRef.
        :type: int
        """
        self._auto_encrypt = auto_encrypt

    @property
    def auto_preheat(self):
        """Gets the auto_preheat of this VideoTypeRef.

        是否自动预热到CDN,取值[0，1]，0表示不自动预热 

        :return: The auto_preheat of this VideoTypeRef.
        :rtype: int
        """
        return self._auto_preheat

    @auto_preheat.setter
    def auto_preheat(self, auto_preheat):
        """Sets the auto_preheat of this VideoTypeRef.

        是否自动预热到CDN,取值[0，1]，0表示不自动预热 

        :param auto_preheat: The auto_preheat of this VideoTypeRef.
        :type: int
        """
        self._auto_preheat = auto_preheat

    @property
    def thumbnail(self):
        """Gets the thumbnail of this VideoTypeRef.


        :return: The thumbnail of this VideoTypeRef.
        :rtype: Thumbnail
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this VideoTypeRef.


        :param thumbnail: The thumbnail of this VideoTypeRef.
        :type: Thumbnail
        """
        self._thumbnail = thumbnail

    @property
    def review(self):
        """Gets the review of this VideoTypeRef.


        :return: The review of this VideoTypeRef.
        :rtype: Review
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this VideoTypeRef.


        :param review: The review of this VideoTypeRef.
        :type: Review
        """
        self._review = review

    @property
    def workflow_name(self):
        """Gets the workflow_name of this VideoTypeRef.

        工作流ID

        :return: The workflow_name of this VideoTypeRef.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this VideoTypeRef.

        工作流ID

        :param workflow_name: The workflow_name of this VideoTypeRef.
        :type: str
        """
        self._workflow_name = workflow_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VideoTypeRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
