# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSnapshotsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'modules': 'list[int]'
    }

    attribute_map = {
        'modules': 'modules'
    }

    def __init__(self, modules=None):
        r"""CreateSnapshotsRequestBody

        The model defined in huaweicloud sdk

        :param modules: 需要创建的snapshot类型，0表示元数据锁，1表示innodb等待锁，2表示最近发生的死锁
        :type modules: list[int]
        """
        
        

        self._modules = None
        self.discriminator = None

        self.modules = modules

    @property
    def modules(self):
        r"""Gets the modules of this CreateSnapshotsRequestBody.

        需要创建的snapshot类型，0表示元数据锁，1表示innodb等待锁，2表示最近发生的死锁

        :return: The modules of this CreateSnapshotsRequestBody.
        :rtype: list[int]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        r"""Sets the modules of this CreateSnapshotsRequestBody.

        需要创建的snapshot类型，0表示元数据锁，1表示innodb等待锁，2表示最近发生的死锁

        :param modules: The modules of this CreateSnapshotsRequestBody.
        :type modules: list[int]
        """
        self._modules = modules

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
        if not isinstance(other, CreateSnapshotsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
