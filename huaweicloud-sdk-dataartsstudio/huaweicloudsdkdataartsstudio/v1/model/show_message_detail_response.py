# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessageDetailResponse(SdkResponse):

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
        'api_apply_status': 'str',
        'api_apply_type': 'str',
        'api_id': 'str',
        'api_name': 'str',
        'api_using_time': 'int',
        'app_id': 'str',
        'app_name': 'str',
        'apply_time': 'int',
        'approval_time': 'int',
        'approver_name': 'str',
        'comment': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'api_apply_status': 'api_apply_status',
        'api_apply_type': 'api_apply_type',
        'api_id': 'api_id',
        'api_name': 'api_name',
        'api_using_time': 'api_using_time',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'apply_time': 'apply_time',
        'approval_time': 'approval_time',
        'approver_name': 'approver_name',
        'comment': 'comment',
        'user_name': 'user_name'
    }

    def __init__(self, id=None, api_apply_status=None, api_apply_type=None, api_id=None, api_name=None, api_using_time=None, app_id=None, app_name=None, apply_time=None, approval_time=None, approver_name=None, comment=None, user_name=None):
        """ShowMessageDetailResponse

        The model defined in huaweicloud sdk

        :param id: 申请编号
        :type id: str
        :param api_apply_status: 申请状态
        :type api_apply_status: str
        :param api_apply_type: 申请类型
        :type api_apply_type: str
        :param api_id: api编号
        :type api_id: str
        :param api_name: api名称
        :type api_name: str
        :param api_using_time: 使用截止时间
        :type api_using_time: int
        :param app_id: app编号
        :type app_id: str
        :param app_name: app名称
        :type app_name: str
        :param apply_time: 申请时间
        :type apply_time: int
        :param approval_time: 授权时间
        :type approval_time: int
        :param approver_name: 审核人名称
        :type approver_name: str
        :param comment: 审核评论
        :type comment: str
        :param user_name: 申请人姓名
        :type user_name: str
        """
        
        super(ShowMessageDetailResponse, self).__init__()

        self._id = None
        self._api_apply_status = None
        self._api_apply_type = None
        self._api_id = None
        self._api_name = None
        self._api_using_time = None
        self._app_id = None
        self._app_name = None
        self._apply_time = None
        self._approval_time = None
        self._approver_name = None
        self._comment = None
        self._user_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if api_apply_status is not None:
            self.api_apply_status = api_apply_status
        if api_apply_type is not None:
            self.api_apply_type = api_apply_type
        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if api_using_time is not None:
            self.api_using_time = api_using_time
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if apply_time is not None:
            self.apply_time = apply_time
        if approval_time is not None:
            self.approval_time = approval_time
        if approver_name is not None:
            self.approver_name = approver_name
        if comment is not None:
            self.comment = comment
        if user_name is not None:
            self.user_name = user_name

    @property
    def id(self):
        """Gets the id of this ShowMessageDetailResponse.

        申请编号

        :return: The id of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowMessageDetailResponse.

        申请编号

        :param id: The id of this ShowMessageDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def api_apply_status(self):
        """Gets the api_apply_status of this ShowMessageDetailResponse.

        申请状态

        :return: The api_apply_status of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._api_apply_status

    @api_apply_status.setter
    def api_apply_status(self, api_apply_status):
        """Sets the api_apply_status of this ShowMessageDetailResponse.

        申请状态

        :param api_apply_status: The api_apply_status of this ShowMessageDetailResponse.
        :type api_apply_status: str
        """
        self._api_apply_status = api_apply_status

    @property
    def api_apply_type(self):
        """Gets the api_apply_type of this ShowMessageDetailResponse.

        申请类型

        :return: The api_apply_type of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._api_apply_type

    @api_apply_type.setter
    def api_apply_type(self, api_apply_type):
        """Sets the api_apply_type of this ShowMessageDetailResponse.

        申请类型

        :param api_apply_type: The api_apply_type of this ShowMessageDetailResponse.
        :type api_apply_type: str
        """
        self._api_apply_type = api_apply_type

    @property
    def api_id(self):
        """Gets the api_id of this ShowMessageDetailResponse.

        api编号

        :return: The api_id of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ShowMessageDetailResponse.

        api编号

        :param api_id: The api_id of this ShowMessageDetailResponse.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        """Gets the api_name of this ShowMessageDetailResponse.

        api名称

        :return: The api_name of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this ShowMessageDetailResponse.

        api名称

        :param api_name: The api_name of this ShowMessageDetailResponse.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def api_using_time(self):
        """Gets the api_using_time of this ShowMessageDetailResponse.

        使用截止时间

        :return: The api_using_time of this ShowMessageDetailResponse.
        :rtype: int
        """
        return self._api_using_time

    @api_using_time.setter
    def api_using_time(self, api_using_time):
        """Sets the api_using_time of this ShowMessageDetailResponse.

        使用截止时间

        :param api_using_time: The api_using_time of this ShowMessageDetailResponse.
        :type api_using_time: int
        """
        self._api_using_time = api_using_time

    @property
    def app_id(self):
        """Gets the app_id of this ShowMessageDetailResponse.

        app编号

        :return: The app_id of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowMessageDetailResponse.

        app编号

        :param app_id: The app_id of this ShowMessageDetailResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this ShowMessageDetailResponse.

        app名称

        :return: The app_name of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowMessageDetailResponse.

        app名称

        :param app_name: The app_name of this ShowMessageDetailResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def apply_time(self):
        """Gets the apply_time of this ShowMessageDetailResponse.

        申请时间

        :return: The apply_time of this ShowMessageDetailResponse.
        :rtype: int
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ShowMessageDetailResponse.

        申请时间

        :param apply_time: The apply_time of this ShowMessageDetailResponse.
        :type apply_time: int
        """
        self._apply_time = apply_time

    @property
    def approval_time(self):
        """Gets the approval_time of this ShowMessageDetailResponse.

        授权时间

        :return: The approval_time of this ShowMessageDetailResponse.
        :rtype: int
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        """Sets the approval_time of this ShowMessageDetailResponse.

        授权时间

        :param approval_time: The approval_time of this ShowMessageDetailResponse.
        :type approval_time: int
        """
        self._approval_time = approval_time

    @property
    def approver_name(self):
        """Gets the approver_name of this ShowMessageDetailResponse.

        审核人名称

        :return: The approver_name of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        """Sets the approver_name of this ShowMessageDetailResponse.

        审核人名称

        :param approver_name: The approver_name of this ShowMessageDetailResponse.
        :type approver_name: str
        """
        self._approver_name = approver_name

    @property
    def comment(self):
        """Gets the comment of this ShowMessageDetailResponse.

        审核评论

        :return: The comment of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ShowMessageDetailResponse.

        审核评论

        :param comment: The comment of this ShowMessageDetailResponse.
        :type comment: str
        """
        self._comment = comment

    @property
    def user_name(self):
        """Gets the user_name of this ShowMessageDetailResponse.

        申请人姓名

        :return: The user_name of this ShowMessageDetailResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowMessageDetailResponse.

        申请人姓名

        :param user_name: The user_name of this ShowMessageDetailResponse.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ShowMessageDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
