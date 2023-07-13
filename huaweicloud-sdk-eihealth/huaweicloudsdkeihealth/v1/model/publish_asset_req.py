# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishAssetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'tag': 'str',
        'name': 'str',
        'version': 'str',
        'title': 'str',
        'picture': 'str',
        'summary': 'str',
        'description': 'str',
        'labels': 'list[str]'
    }

    attribute_map = {
        'image_id': 'image_id',
        'tag': 'tag',
        'name': 'name',
        'version': 'version',
        'title': 'title',
        'picture': 'picture',
        'summary': 'summary',
        'description': 'description',
        'labels': 'labels'
    }

    def __init__(self, image_id=None, tag=None, name=None, version=None, title=None, picture=None, summary=None, description=None, labels=None):
        """PublishAssetReq

        The model defined in huaweicloud sdk

        :param image_id: 镜像id
        :type image_id: str
        :param tag: 镜像tag
        :type tag: str
        :param name: 资产名称
        :type name: str
        :param version: 资产版本
        :type version: str
        :param title: 展示名
        :type title: str
        :param picture: 封面图片base64编码
        :type picture: str
        :param summary: 短描述
        :type summary: str
        :param description: 长描述
        :type description: str
        :param labels: 标签列表
        :type labels: list[str]
        """
        
        

        self._image_id = None
        self._tag = None
        self._name = None
        self._version = None
        self._title = None
        self._picture = None
        self._summary = None
        self._description = None
        self._labels = None
        self.discriminator = None

        self.image_id = image_id
        self.tag = tag
        self.name = name
        self.version = version
        if title is not None:
            self.title = title
        if picture is not None:
            self.picture = picture
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels

    @property
    def image_id(self):
        """Gets the image_id of this PublishAssetReq.

        镜像id

        :return: The image_id of this PublishAssetReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this PublishAssetReq.

        镜像id

        :param image_id: The image_id of this PublishAssetReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def tag(self):
        """Gets the tag of this PublishAssetReq.

        镜像tag

        :return: The tag of this PublishAssetReq.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PublishAssetReq.

        镜像tag

        :param tag: The tag of this PublishAssetReq.
        :type tag: str
        """
        self._tag = tag

    @property
    def name(self):
        """Gets the name of this PublishAssetReq.

        资产名称

        :return: The name of this PublishAssetReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublishAssetReq.

        资产名称

        :param name: The name of this PublishAssetReq.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this PublishAssetReq.

        资产版本

        :return: The version of this PublishAssetReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PublishAssetReq.

        资产版本

        :param version: The version of this PublishAssetReq.
        :type version: str
        """
        self._version = version

    @property
    def title(self):
        """Gets the title of this PublishAssetReq.

        展示名

        :return: The title of this PublishAssetReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PublishAssetReq.

        展示名

        :param title: The title of this PublishAssetReq.
        :type title: str
        """
        self._title = title

    @property
    def picture(self):
        """Gets the picture of this PublishAssetReq.

        封面图片base64编码

        :return: The picture of this PublishAssetReq.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this PublishAssetReq.

        封面图片base64编码

        :param picture: The picture of this PublishAssetReq.
        :type picture: str
        """
        self._picture = picture

    @property
    def summary(self):
        """Gets the summary of this PublishAssetReq.

        短描述

        :return: The summary of this PublishAssetReq.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this PublishAssetReq.

        短描述

        :param summary: The summary of this PublishAssetReq.
        :type summary: str
        """
        self._summary = summary

    @property
    def description(self):
        """Gets the description of this PublishAssetReq.

        长描述

        :return: The description of this PublishAssetReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PublishAssetReq.

        长描述

        :param description: The description of this PublishAssetReq.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this PublishAssetReq.

        标签列表

        :return: The labels of this PublishAssetReq.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PublishAssetReq.

        标签列表

        :param labels: The labels of this PublishAssetReq.
        :type labels: list[str]
        """
        self._labels = labels

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublishAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
