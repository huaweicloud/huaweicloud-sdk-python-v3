# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelPageListDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'feature': 'str',
        'labels': 'list[str]',
        'creator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'feature': 'feature',
        'labels': 'labels',
        'creator': 'creator'
    }

    def __init__(self, id=None, name=None, feature=None, labels=None, creator=None):
        """LabelPageListDto

        The model defined in huaweicloud sdk

        :param id: 标签页面id
        :type id: str
        :param name: 标签页面标题
        :type name: str
        :param feature: 标签页面类型
        :type feature: str
        :param labels: 标签页面包含的标签
        :type labels: list[str]
        :param creator: 标签页面创建者
        :type creator: str
        """
        
        

        self._id = None
        self._name = None
        self._feature = None
        self._labels = None
        self._creator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if feature is not None:
            self.feature = feature
        if labels is not None:
            self.labels = labels
        if creator is not None:
            self.creator = creator

    @property
    def id(self):
        """Gets the id of this LabelPageListDto.

        标签页面id

        :return: The id of this LabelPageListDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LabelPageListDto.

        标签页面id

        :param id: The id of this LabelPageListDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this LabelPageListDto.

        标签页面标题

        :return: The name of this LabelPageListDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabelPageListDto.

        标签页面标题

        :param name: The name of this LabelPageListDto.
        :type name: str
        """
        self._name = name

    @property
    def feature(self):
        """Gets the feature of this LabelPageListDto.

        标签页面类型

        :return: The feature of this LabelPageListDto.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this LabelPageListDto.

        标签页面类型

        :param feature: The feature of this LabelPageListDto.
        :type feature: str
        """
        self._feature = feature

    @property
    def labels(self):
        """Gets the labels of this LabelPageListDto.

        标签页面包含的标签

        :return: The labels of this LabelPageListDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this LabelPageListDto.

        标签页面包含的标签

        :param labels: The labels of this LabelPageListDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def creator(self):
        """Gets the creator of this LabelPageListDto.

        标签页面创建者

        :return: The creator of this LabelPageListDto.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this LabelPageListDto.

        标签页面创建者

        :param creator: The creator of this LabelPageListDto.
        :type creator: str
        """
        self._creator = creator

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
        if not isinstance(other, LabelPageListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
