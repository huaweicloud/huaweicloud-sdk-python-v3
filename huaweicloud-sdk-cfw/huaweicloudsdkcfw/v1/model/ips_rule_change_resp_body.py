# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsRuleChangeRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'group_id': 'str',
        'id': 'str',
        'ips_ids': 'list[str]',
        'result': 'bool'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'group_id': 'group_id',
        'id': 'id',
        'ips_ids': 'ips_ids',
        'result': 'result'
    }

    def __init__(self, error_code=None, error_msg=None, group_id=None, id=None, ips_ids=None, result=None):
        r"""IpsRuleChangeRespBody

        The model defined in huaweicloud sdk

        :param error_code: 错误代码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param group_id: 分组id
        :type group_id: str
        :param id: 防火墙id
        :type id: str
        :param ips_ids: ips的id列表
        :type ips_ids: list[str]
        :param result: 修改结果
        :type result: bool
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._group_id = None
        self._id = None
        self._ips_ids = None
        self._result = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if ips_ids is not None:
            self.ips_ids = ips_ids
        if result is not None:
            self.result = result

    @property
    def error_code(self):
        r"""Gets the error_code of this IpsRuleChangeRespBody.

        错误代码

        :return: The error_code of this IpsRuleChangeRespBody.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this IpsRuleChangeRespBody.

        错误代码

        :param error_code: The error_code of this IpsRuleChangeRespBody.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this IpsRuleChangeRespBody.

        错误信息

        :return: The error_msg of this IpsRuleChangeRespBody.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this IpsRuleChangeRespBody.

        错误信息

        :param error_msg: The error_msg of this IpsRuleChangeRespBody.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def group_id(self):
        r"""Gets the group_id of this IpsRuleChangeRespBody.

        分组id

        :return: The group_id of this IpsRuleChangeRespBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this IpsRuleChangeRespBody.

        分组id

        :param group_id: The group_id of this IpsRuleChangeRespBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def id(self):
        r"""Gets the id of this IpsRuleChangeRespBody.

        防火墙id

        :return: The id of this IpsRuleChangeRespBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IpsRuleChangeRespBody.

        防火墙id

        :param id: The id of this IpsRuleChangeRespBody.
        :type id: str
        """
        self._id = id

    @property
    def ips_ids(self):
        r"""Gets the ips_ids of this IpsRuleChangeRespBody.

        ips的id列表

        :return: The ips_ids of this IpsRuleChangeRespBody.
        :rtype: list[str]
        """
        return self._ips_ids

    @ips_ids.setter
    def ips_ids(self, ips_ids):
        r"""Sets the ips_ids of this IpsRuleChangeRespBody.

        ips的id列表

        :param ips_ids: The ips_ids of this IpsRuleChangeRespBody.
        :type ips_ids: list[str]
        """
        self._ips_ids = ips_ids

    @property
    def result(self):
        r"""Gets the result of this IpsRuleChangeRespBody.

        修改结果

        :return: The result of this IpsRuleChangeRespBody.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this IpsRuleChangeRespBody.

        修改结果

        :param result: The result of this IpsRuleChangeRespBody.
        :type result: bool
        """
        self._result = result

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
        if not isinstance(other, IpsRuleChangeRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
