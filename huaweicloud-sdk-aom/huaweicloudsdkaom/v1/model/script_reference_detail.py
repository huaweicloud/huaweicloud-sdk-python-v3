# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptReferenceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reference_name': 'str',
        'reference_id': 'str',
        'reference_type': 'str'
    }

    attribute_map = {
        'reference_name': 'reference_name',
        'reference_id': 'reference_id',
        'reference_type': 'reference_type'
    }

    def __init__(self, reference_name=None, reference_id=None, reference_type=None):
        """ScriptReferenceDetail

        The model defined in huaweicloud sdk

        :param reference_name: 引用的任务名称
        :type reference_name: str
        :param reference_id: 引用id
        :type reference_id: str
        :param reference_type: 引用的任务类型
        :type reference_type: str
        """
        
        

        self._reference_name = None
        self._reference_id = None
        self._reference_type = None
        self.discriminator = None

        if reference_name is not None:
            self.reference_name = reference_name
        if reference_id is not None:
            self.reference_id = reference_id
        if reference_type is not None:
            self.reference_type = reference_type

    @property
    def reference_name(self):
        """Gets the reference_name of this ScriptReferenceDetail.

        引用的任务名称

        :return: The reference_name of this ScriptReferenceDetail.
        :rtype: str
        """
        return self._reference_name

    @reference_name.setter
    def reference_name(self, reference_name):
        """Sets the reference_name of this ScriptReferenceDetail.

        引用的任务名称

        :param reference_name: The reference_name of this ScriptReferenceDetail.
        :type reference_name: str
        """
        self._reference_name = reference_name

    @property
    def reference_id(self):
        """Gets the reference_id of this ScriptReferenceDetail.

        引用id

        :return: The reference_id of this ScriptReferenceDetail.
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this ScriptReferenceDetail.

        引用id

        :param reference_id: The reference_id of this ScriptReferenceDetail.
        :type reference_id: str
        """
        self._reference_id = reference_id

    @property
    def reference_type(self):
        """Gets the reference_type of this ScriptReferenceDetail.

        引用的任务类型

        :return: The reference_type of this ScriptReferenceDetail.
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this ScriptReferenceDetail.

        引用的任务类型

        :param reference_type: The reference_type of this ScriptReferenceDetail.
        :type reference_type: str
        """
        self._reference_type = reference_type

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
        if not isinstance(other, ScriptReferenceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
