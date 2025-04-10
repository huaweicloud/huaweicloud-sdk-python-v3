# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RdsDbResponseRetList:

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
        'ret_status': 'str',
        'ret_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ret_status': 'ret_status',
        'ret_message': 'ret_message'
    }

    def __init__(self, id=None, ret_status=None, ret_message=None):
        r"""RdsDbResponseRetList

        The model defined in huaweicloud sdk

        :param id: rds数据库id
        :type id: str
        :param ret_status: 状态 - SUCCESS - FAILED
        :type ret_status: str
        :param ret_message: 描述
        :type ret_message: str
        """
        
        

        self._id = None
        self._ret_status = None
        self._ret_message = None
        self.discriminator = None

        self.id = id
        self.ret_status = ret_status
        self.ret_message = ret_message

    @property
    def id(self):
        r"""Gets the id of this RdsDbResponseRetList.

        rds数据库id

        :return: The id of this RdsDbResponseRetList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RdsDbResponseRetList.

        rds数据库id

        :param id: The id of this RdsDbResponseRetList.
        :type id: str
        """
        self._id = id

    @property
    def ret_status(self):
        r"""Gets the ret_status of this RdsDbResponseRetList.

        状态 - SUCCESS - FAILED

        :return: The ret_status of this RdsDbResponseRetList.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        r"""Sets the ret_status of this RdsDbResponseRetList.

        状态 - SUCCESS - FAILED

        :param ret_status: The ret_status of this RdsDbResponseRetList.
        :type ret_status: str
        """
        self._ret_status = ret_status

    @property
    def ret_message(self):
        r"""Gets the ret_message of this RdsDbResponseRetList.

        描述

        :return: The ret_message of this RdsDbResponseRetList.
        :rtype: str
        """
        return self._ret_message

    @ret_message.setter
    def ret_message(self, ret_message):
        r"""Sets the ret_message of this RdsDbResponseRetList.

        描述

        :param ret_message: The ret_message of this RdsDbResponseRetList.
        :type ret_message: str
        """
        self._ret_message = ret_message

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
        if not isinstance(other, RdsDbResponseRetList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
