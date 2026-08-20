# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateRespDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue_id': 'str',
        'fail_msg': 'str',
        'operation_flag': 'int',
        'modified_date': 'int',
        'modified_by': 'str'
    }

    attribute_map = {
        'issue_id': 'issue_id',
        'fail_msg': 'fail_msg',
        'operation_flag': 'operation_flag',
        'modified_date': 'modified_date',
        'modified_by': 'modified_by'
    }

    def __init__(self, issue_id=None, fail_msg=None, operation_flag=None, modified_date=None, modified_by=None):
        r"""AssociateRespDetail

        The model defined in huaweicloud sdk

        :param issue_id: 关联的工作项ID，多个ID使用逗号分割。
        :type issue_id: str
        :param fail_msg: 失败原因。
        :type fail_msg: str
        :param operation_flag: 操作类型标记位。
        :type operation_flag: int
        :param modified_date: 修改日期。
        :type modified_date: int
        :param modified_by: 修改人。
        :type modified_by: str
        """
        
        

        self._issue_id = None
        self._fail_msg = None
        self._operation_flag = None
        self._modified_date = None
        self._modified_by = None
        self.discriminator = None

        if issue_id is not None:
            self.issue_id = issue_id
        if fail_msg is not None:
            self.fail_msg = fail_msg
        if operation_flag is not None:
            self.operation_flag = operation_flag
        if modified_date is not None:
            self.modified_date = modified_date
        if modified_by is not None:
            self.modified_by = modified_by

    @property
    def issue_id(self):
        r"""Gets the issue_id of this AssociateRespDetail.

        关联的工作项ID，多个ID使用逗号分割。

        :return: The issue_id of this AssociateRespDetail.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this AssociateRespDetail.

        关联的工作项ID，多个ID使用逗号分割。

        :param issue_id: The issue_id of this AssociateRespDetail.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def fail_msg(self):
        r"""Gets the fail_msg of this AssociateRespDetail.

        失败原因。

        :return: The fail_msg of this AssociateRespDetail.
        :rtype: str
        """
        return self._fail_msg

    @fail_msg.setter
    def fail_msg(self, fail_msg):
        r"""Sets the fail_msg of this AssociateRespDetail.

        失败原因。

        :param fail_msg: The fail_msg of this AssociateRespDetail.
        :type fail_msg: str
        """
        self._fail_msg = fail_msg

    @property
    def operation_flag(self):
        r"""Gets the operation_flag of this AssociateRespDetail.

        操作类型标记位。

        :return: The operation_flag of this AssociateRespDetail.
        :rtype: int
        """
        return self._operation_flag

    @operation_flag.setter
    def operation_flag(self, operation_flag):
        r"""Sets the operation_flag of this AssociateRespDetail.

        操作类型标记位。

        :param operation_flag: The operation_flag of this AssociateRespDetail.
        :type operation_flag: int
        """
        self._operation_flag = operation_flag

    @property
    def modified_date(self):
        r"""Gets the modified_date of this AssociateRespDetail.

        修改日期。

        :return: The modified_date of this AssociateRespDetail.
        :rtype: int
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this AssociateRespDetail.

        修改日期。

        :param modified_date: The modified_date of this AssociateRespDetail.
        :type modified_date: int
        """
        self._modified_date = modified_date

    @property
    def modified_by(self):
        r"""Gets the modified_by of this AssociateRespDetail.

        修改人。

        :return: The modified_by of this AssociateRespDetail.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this AssociateRespDetail.

        修改人。

        :param modified_by: The modified_by of this AssociateRespDetail.
        :type modified_by: str
        """
        self._modified_by = modified_by

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssociateRespDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
