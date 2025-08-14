# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuthorizationMailRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'app_group_id': 'str',
        'account': 'str',
        'mail_send_type': 'str',
        'mail_send_result': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'app_group_id': 'app_group_id',
        'account': 'account',
        'mail_send_type': 'mail_send_type',
        'mail_send_result': 'mail_send_result'
    }

    def __init__(self, limit=None, offset=None, app_group_id=None, account=None, mail_send_type=None, mail_send_result=None):
        r"""ListAuthorizationMailRecordRequest

        The model defined in huaweicloud sdk

        :param limit: 单次查询的大小[1-100]，默认值10。
        :type limit: int
        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param app_group_id: 应用组ID。
        :type app_group_id: str
        :param account: 用户(组)名称。
        :type account: str
        :param mail_send_type: 授权类型： - ADD_GROUP_AUTHORIZATION 添加组授权 - DEL_GROUP_AUTHORIZATION 删除组授权。
        :type mail_send_type: str
        :param mail_send_result: 邮件发送结果(SUCCESS|FAIL)。
        :type mail_send_result: str
        """
        
        

        self._limit = None
        self._offset = None
        self._app_group_id = None
        self._account = None
        self._mail_send_type = None
        self._mail_send_result = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.app_group_id = app_group_id
        if account is not None:
            self.account = account
        if mail_send_type is not None:
            self.mail_send_type = mail_send_type
        if mail_send_result is not None:
            self.mail_send_result = mail_send_result

    @property
    def limit(self):
        r"""Gets the limit of this ListAuthorizationMailRecordRequest.

        单次查询的大小[1-100]，默认值10。

        :return: The limit of this ListAuthorizationMailRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAuthorizationMailRecordRequest.

        单次查询的大小[1-100]，默认值10。

        :param limit: The limit of this ListAuthorizationMailRecordRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAuthorizationMailRecordRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListAuthorizationMailRecordRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAuthorizationMailRecordRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListAuthorizationMailRecordRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def app_group_id(self):
        r"""Gets the app_group_id of this ListAuthorizationMailRecordRequest.

        应用组ID。

        :return: The app_group_id of this ListAuthorizationMailRecordRequest.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        r"""Sets the app_group_id of this ListAuthorizationMailRecordRequest.

        应用组ID。

        :param app_group_id: The app_group_id of this ListAuthorizationMailRecordRequest.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def account(self):
        r"""Gets the account of this ListAuthorizationMailRecordRequest.

        用户(组)名称。

        :return: The account of this ListAuthorizationMailRecordRequest.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this ListAuthorizationMailRecordRequest.

        用户(组)名称。

        :param account: The account of this ListAuthorizationMailRecordRequest.
        :type account: str
        """
        self._account = account

    @property
    def mail_send_type(self):
        r"""Gets the mail_send_type of this ListAuthorizationMailRecordRequest.

        授权类型： - ADD_GROUP_AUTHORIZATION 添加组授权 - DEL_GROUP_AUTHORIZATION 删除组授权。

        :return: The mail_send_type of this ListAuthorizationMailRecordRequest.
        :rtype: str
        """
        return self._mail_send_type

    @mail_send_type.setter
    def mail_send_type(self, mail_send_type):
        r"""Sets the mail_send_type of this ListAuthorizationMailRecordRequest.

        授权类型： - ADD_GROUP_AUTHORIZATION 添加组授权 - DEL_GROUP_AUTHORIZATION 删除组授权。

        :param mail_send_type: The mail_send_type of this ListAuthorizationMailRecordRequest.
        :type mail_send_type: str
        """
        self._mail_send_type = mail_send_type

    @property
    def mail_send_result(self):
        r"""Gets the mail_send_result of this ListAuthorizationMailRecordRequest.

        邮件发送结果(SUCCESS|FAIL)。

        :return: The mail_send_result of this ListAuthorizationMailRecordRequest.
        :rtype: str
        """
        return self._mail_send_result

    @mail_send_result.setter
    def mail_send_result(self, mail_send_result):
        r"""Sets the mail_send_result of this ListAuthorizationMailRecordRequest.

        邮件发送结果(SUCCESS|FAIL)。

        :param mail_send_result: The mail_send_result of this ListAuthorizationMailRecordRequest.
        :type mail_send_result: str
        """
        self._mail_send_result = mail_send_result

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
        if not isinstance(other, ListAuthorizationMailRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
