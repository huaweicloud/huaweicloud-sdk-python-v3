# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCategoryReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'parent_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'parent_id': 'parent_id'
    }

    def __init__(self, name=None, parent_id=None):
        """CreateCategoryReq

        The model defined in huaweicloud sdk

        :param name: 媒资分类名称，最大64字节。
        :type name: str
        :param parent_id: 父分类ID。  若不填，则默认生成一级分类。  根节点分类ID为0。
        :type parent_id: int
        """
        
        

        self._name = None
        self._parent_id = None
        self.discriminator = None

        self.name = name
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this CreateCategoryReq.

        媒资分类名称，最大64字节。

        :return: The name of this CreateCategoryReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCategoryReq.

        媒资分类名称，最大64字节。

        :param name: The name of this CreateCategoryReq.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateCategoryReq.

        父分类ID。  若不填，则默认生成一级分类。  根节点分类ID为0。

        :return: The parent_id of this CreateCategoryReq.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateCategoryReq.

        父分类ID。  若不填，则默认生成一级分类。  根节点分类ID为0。

        :param parent_id: The parent_id of this CreateCategoryReq.
        :type parent_id: int
        """
        self._parent_id = parent_id

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
        if not isinstance(other, CreateCategoryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
