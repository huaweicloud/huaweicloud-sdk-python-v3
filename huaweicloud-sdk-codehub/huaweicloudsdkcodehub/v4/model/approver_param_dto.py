# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApproverParamDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approver_id': 'int',
        'code_owner': 'bool',
        'accept': 'bool'
    }

    attribute_map = {
        'approver_id': 'approver_id',
        'code_owner': 'code_owner',
        'accept': 'accept'
    }

    def __init__(self, approver_id=None, code_owner=None, accept=None):
        r"""ApproverParamDto

        The model defined in huaweicloud sdk

        :param approver_id: 审核人id
        :type approver_id: int
        :param code_owner: 代码所有者
        :type code_owner: bool
        :param accept: 是否接纳
        :type accept: bool
        """
        
        

        self._approver_id = None
        self._code_owner = None
        self._accept = None
        self.discriminator = None

        if approver_id is not None:
            self.approver_id = approver_id
        if code_owner is not None:
            self.code_owner = code_owner
        if accept is not None:
            self.accept = accept

    @property
    def approver_id(self):
        r"""Gets the approver_id of this ApproverParamDto.

        审核人id

        :return: The approver_id of this ApproverParamDto.
        :rtype: int
        """
        return self._approver_id

    @approver_id.setter
    def approver_id(self, approver_id):
        r"""Sets the approver_id of this ApproverParamDto.

        审核人id

        :param approver_id: The approver_id of this ApproverParamDto.
        :type approver_id: int
        """
        self._approver_id = approver_id

    @property
    def code_owner(self):
        r"""Gets the code_owner of this ApproverParamDto.

        代码所有者

        :return: The code_owner of this ApproverParamDto.
        :rtype: bool
        """
        return self._code_owner

    @code_owner.setter
    def code_owner(self, code_owner):
        r"""Sets the code_owner of this ApproverParamDto.

        代码所有者

        :param code_owner: The code_owner of this ApproverParamDto.
        :type code_owner: bool
        """
        self._code_owner = code_owner

    @property
    def accept(self):
        r"""Gets the accept of this ApproverParamDto.

        是否接纳

        :return: The accept of this ApproverParamDto.
        :rtype: bool
        """
        return self._accept

    @accept.setter
    def accept(self, accept):
        r"""Sets the accept of this ApproverParamDto.

        是否接纳

        :param accept: The accept of this ApproverParamDto.
        :type accept: bool
        """
        self._accept = accept

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
        if not isinstance(other, ApproverParamDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
