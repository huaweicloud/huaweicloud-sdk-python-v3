# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppBaseInfo:

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
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'remark': 'remark'
    }

    def __init__(self, id=None, name=None, remark=None):
        """AppBaseInfo

        The model defined in huaweicloud sdk

        :param id: 编号
        :type id: str
        :param name: 名称
        :type name: str
        :param remark: 描述
        :type remark: str
        """
        
        

        self._id = None
        self._name = None
        self._remark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        """Gets the id of this AppBaseInfo.

        编号

        :return: The id of this AppBaseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppBaseInfo.

        编号

        :param id: The id of this AppBaseInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AppBaseInfo.

        名称

        :return: The name of this AppBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppBaseInfo.

        名称

        :param name: The name of this AppBaseInfo.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this AppBaseInfo.

        描述

        :return: The remark of this AppBaseInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AppBaseInfo.

        描述

        :param remark: The remark of this AppBaseInfo.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, AppBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
