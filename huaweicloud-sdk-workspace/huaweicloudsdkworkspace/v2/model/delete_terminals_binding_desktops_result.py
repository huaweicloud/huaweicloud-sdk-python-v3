# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTerminalsBindingDesktopsResult:

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
        'delete_result_code': 'str',
        'delete_result_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'delete_result_code': 'delete_result_code',
        'delete_result_msg': 'delete_result_msg'
    }

    def __init__(self, id=None, delete_result_code=None, delete_result_msg=None):
        """DeleteTerminalsBindingDesktopsResult

        The model defined in huaweicloud sdk

        :param id: 需删除的策略ID
        :type id: str
        :param delete_result_code: 删除操作的结果码
        :type delete_result_code: str
        :param delete_result_msg: 删除操作的结果信息
        :type delete_result_msg: str
        """
        
        

        self._id = None
        self._delete_result_code = None
        self._delete_result_msg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if delete_result_code is not None:
            self.delete_result_code = delete_result_code
        if delete_result_msg is not None:
            self.delete_result_msg = delete_result_msg

    @property
    def id(self):
        """Gets the id of this DeleteTerminalsBindingDesktopsResult.

        需删除的策略ID

        :return: The id of this DeleteTerminalsBindingDesktopsResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteTerminalsBindingDesktopsResult.

        需删除的策略ID

        :param id: The id of this DeleteTerminalsBindingDesktopsResult.
        :type id: str
        """
        self._id = id

    @property
    def delete_result_code(self):
        """Gets the delete_result_code of this DeleteTerminalsBindingDesktopsResult.

        删除操作的结果码

        :return: The delete_result_code of this DeleteTerminalsBindingDesktopsResult.
        :rtype: str
        """
        return self._delete_result_code

    @delete_result_code.setter
    def delete_result_code(self, delete_result_code):
        """Sets the delete_result_code of this DeleteTerminalsBindingDesktopsResult.

        删除操作的结果码

        :param delete_result_code: The delete_result_code of this DeleteTerminalsBindingDesktopsResult.
        :type delete_result_code: str
        """
        self._delete_result_code = delete_result_code

    @property
    def delete_result_msg(self):
        """Gets the delete_result_msg of this DeleteTerminalsBindingDesktopsResult.

        删除操作的结果信息

        :return: The delete_result_msg of this DeleteTerminalsBindingDesktopsResult.
        :rtype: str
        """
        return self._delete_result_msg

    @delete_result_msg.setter
    def delete_result_msg(self, delete_result_msg):
        """Sets the delete_result_msg of this DeleteTerminalsBindingDesktopsResult.

        删除操作的结果信息

        :param delete_result_msg: The delete_result_msg of this DeleteTerminalsBindingDesktopsResult.
        :type delete_result_msg: str
        """
        self._delete_result_msg = delete_result_msg

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
        if not isinstance(other, DeleteTerminalsBindingDesktopsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
