# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlJobTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'sql_id': 'str',
        'group': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'sql_id': 'sql_id',
        'group': 'group'
    }

    def __init__(self, is_success=None, message=None, sql_id=None, group=None):
        r"""CreateSqlJobTemplateResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。执行失败时，用于显示执行失败的原因。
        :type message: str
        :param sql_id: 新增SQL模板的ID。
        :type sql_id: str
        :param group: SQL模板分组名称。
        :type group: str
        """
        
        super(CreateSqlJobTemplateResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._sql_id = None
        self._group = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if sql_id is not None:
            self.sql_id = sql_id
        if group is not None:
            self.group = group

    @property
    def is_success(self):
        r"""Gets the is_success of this CreateSqlJobTemplateResponse.

        是否成功。

        :return: The is_success of this CreateSqlJobTemplateResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this CreateSqlJobTemplateResponse.

        是否成功。

        :param is_success: The is_success of this CreateSqlJobTemplateResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this CreateSqlJobTemplateResponse.

        系统提示信息，执行成功时，信息可能为空。执行失败时，用于显示执行失败的原因。

        :return: The message of this CreateSqlJobTemplateResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateSqlJobTemplateResponse.

        系统提示信息，执行成功时，信息可能为空。执行失败时，用于显示执行失败的原因。

        :param message: The message of this CreateSqlJobTemplateResponse.
        :type message: str
        """
        self._message = message

    @property
    def sql_id(self):
        r"""Gets the sql_id of this CreateSqlJobTemplateResponse.

        新增SQL模板的ID。

        :return: The sql_id of this CreateSqlJobTemplateResponse.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this CreateSqlJobTemplateResponse.

        新增SQL模板的ID。

        :param sql_id: The sql_id of this CreateSqlJobTemplateResponse.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def group(self):
        r"""Gets the group of this CreateSqlJobTemplateResponse.

        SQL模板分组名称。

        :return: The group of this CreateSqlJobTemplateResponse.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this CreateSqlJobTemplateResponse.

        SQL模板分组名称。

        :param group: The group of this CreateSqlJobTemplateResponse.
        :type group: str
        """
        self._group = group

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
        if not isinstance(other, CreateSqlJobTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
