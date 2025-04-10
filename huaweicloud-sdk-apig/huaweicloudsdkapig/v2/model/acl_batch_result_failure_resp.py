# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AclBatchResultFailureResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'acl_id': 'str',
        'acl_name': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'acl_id': 'acl_id',
        'acl_name': 'acl_name',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, acl_id=None, acl_name=None, error_code=None, error_msg=None):
        r"""AclBatchResultFailureResp

        The model defined in huaweicloud sdk

        :param acl_id: 删除失败的ACL策略ID
        :type acl_id: str
        :param acl_name: 删除失败的ACL策略名称
        :type acl_name: str
        :param error_code: 删除失败的错误码
        :type error_code: str
        :param error_msg: 删除失败的错误信息
        :type error_msg: str
        """
        
        

        self._acl_id = None
        self._acl_name = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if acl_id is not None:
            self.acl_id = acl_id
        if acl_name is not None:
            self.acl_name = acl_name
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def acl_id(self):
        r"""Gets the acl_id of this AclBatchResultFailureResp.

        删除失败的ACL策略ID

        :return: The acl_id of this AclBatchResultFailureResp.
        :rtype: str
        """
        return self._acl_id

    @acl_id.setter
    def acl_id(self, acl_id):
        r"""Sets the acl_id of this AclBatchResultFailureResp.

        删除失败的ACL策略ID

        :param acl_id: The acl_id of this AclBatchResultFailureResp.
        :type acl_id: str
        """
        self._acl_id = acl_id

    @property
    def acl_name(self):
        r"""Gets the acl_name of this AclBatchResultFailureResp.

        删除失败的ACL策略名称

        :return: The acl_name of this AclBatchResultFailureResp.
        :rtype: str
        """
        return self._acl_name

    @acl_name.setter
    def acl_name(self, acl_name):
        r"""Sets the acl_name of this AclBatchResultFailureResp.

        删除失败的ACL策略名称

        :param acl_name: The acl_name of this AclBatchResultFailureResp.
        :type acl_name: str
        """
        self._acl_name = acl_name

    @property
    def error_code(self):
        r"""Gets the error_code of this AclBatchResultFailureResp.

        删除失败的错误码

        :return: The error_code of this AclBatchResultFailureResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this AclBatchResultFailureResp.

        删除失败的错误码

        :param error_code: The error_code of this AclBatchResultFailureResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this AclBatchResultFailureResp.

        删除失败的错误信息

        :return: The error_msg of this AclBatchResultFailureResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this AclBatchResultFailureResp.

        删除失败的错误信息

        :param error_msg: The error_msg of this AclBatchResultFailureResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, AclBatchResultFailureResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
