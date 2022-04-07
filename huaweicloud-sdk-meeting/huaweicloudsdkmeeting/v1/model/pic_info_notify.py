# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PicInfoNotify:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'index': 'int',
        'id': 'list[str]',
        'share': 'int'
    }

    attribute_map = {
        'index': 'index',
        'id': 'id',
        'share': 'share'
    }

    def __init__(self, index=None, id=None, share=None):
        """PicInfoNotify - a model defined in huaweicloud sdk"""
        
        

        self._index = None
        self._id = None
        self._share = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if id is not None:
            self.id = id
        if share is not None:
            self.share = share

    @property
    def index(self):
        """Gets the index of this PicInfoNotify.

        多画面中每个画面的编号，编号从1开始

        :return: The index of this PicInfoNotify.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this PicInfoNotify.

        多画面中每个画面的编号，编号从1开始

        :param index: The index of this PicInfoNotify.
        :type: int
        """
        self._index = index

    @property
    def id(self):
        """Gets the id of this PicInfoNotify.

        每个画面中会话标识，即callNumber。

        :return: The id of this PicInfoNotify.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PicInfoNotify.

        每个画面中会话标识，即callNumber。

        :param id: The id of this PicInfoNotify.
        :type: list[str]
        """
        self._id = id

    @property
    def share(self):
        """Gets the share of this PicInfoNotify.

        是否为辅流 0： 不是辅流 1： 是辅流

        :return: The share of this PicInfoNotify.
        :rtype: int
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this PicInfoNotify.

        是否为辅流 0： 不是辅流 1： 是辅流

        :param share: The share of this PicInfoNotify.
        :type: int
        """
        self._share = share

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
        if not isinstance(other, PicInfoNotify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other