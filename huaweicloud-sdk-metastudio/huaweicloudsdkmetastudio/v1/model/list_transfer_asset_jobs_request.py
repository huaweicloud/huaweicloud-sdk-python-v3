# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransferAssetJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'x_app_user_id': 'str',
        'role': 'str',
        'state': 'str',
        'transfer_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'x_app_user_id': 'X-App-UserId',
        'role': 'role',
        'state': 'state',
        'transfer_type': 'transfer_type'
    }

    def __init__(self, offset=None, limit=None, x_app_user_id=None, role=None, state=None, transfer_type=None):
        r"""ListTransferAssetJobsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param role: 角色。 SENDER:发起方，RECEIVER：接收方。ALL全部
        :type role: str
        :param state: 任务状态。多个状态使用英文逗号分隔。 - PROCESSING: 处理过程中 - ACCEPT： 接受 - REJECT： 拒绝 - CANCEL：取消 - FAIL: 失败
        :type state: str
        :param transfer_type: 任务类型。默认查询TRANSFER_OUT类型任务。 - TRANSFER_OUT: 资产转出 - TRANSFER_BACK： 资产转回
        :type transfer_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._x_app_user_id = None
        self._role = None
        self._state = None
        self._transfer_type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if role is not None:
            self.role = role
        if state is not None:
            self.state = state
        if transfer_type is not None:
            self.transfer_type = transfer_type

    @property
    def offset(self):
        r"""Gets the offset of this ListTransferAssetJobsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListTransferAssetJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTransferAssetJobsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListTransferAssetJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTransferAssetJobsRequest.

        每页显示的条目数量。

        :return: The limit of this ListTransferAssetJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTransferAssetJobsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListTransferAssetJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListTransferAssetJobsRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListTransferAssetJobsRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListTransferAssetJobsRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListTransferAssetJobsRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def role(self):
        r"""Gets the role of this ListTransferAssetJobsRequest.

        角色。 SENDER:发起方，RECEIVER：接收方。ALL全部

        :return: The role of this ListTransferAssetJobsRequest.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ListTransferAssetJobsRequest.

        角色。 SENDER:发起方，RECEIVER：接收方。ALL全部

        :param role: The role of this ListTransferAssetJobsRequest.
        :type role: str
        """
        self._role = role

    @property
    def state(self):
        r"""Gets the state of this ListTransferAssetJobsRequest.

        任务状态。多个状态使用英文逗号分隔。 - PROCESSING: 处理过程中 - ACCEPT： 接受 - REJECT： 拒绝 - CANCEL：取消 - FAIL: 失败

        :return: The state of this ListTransferAssetJobsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListTransferAssetJobsRequest.

        任务状态。多个状态使用英文逗号分隔。 - PROCESSING: 处理过程中 - ACCEPT： 接受 - REJECT： 拒绝 - CANCEL：取消 - FAIL: 失败

        :param state: The state of this ListTransferAssetJobsRequest.
        :type state: str
        """
        self._state = state

    @property
    def transfer_type(self):
        r"""Gets the transfer_type of this ListTransferAssetJobsRequest.

        任务类型。默认查询TRANSFER_OUT类型任务。 - TRANSFER_OUT: 资产转出 - TRANSFER_BACK： 资产转回

        :return: The transfer_type of this ListTransferAssetJobsRequest.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        r"""Sets the transfer_type of this ListTransferAssetJobsRequest.

        任务类型。默认查询TRANSFER_OUT类型任务。 - TRANSFER_OUT: 资产转出 - TRANSFER_BACK： 资产转回

        :param transfer_type: The transfer_type of this ListTransferAssetJobsRequest.
        :type transfer_type: str
        """
        self._transfer_type = transfer_type

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
        if not isinstance(other, ListTransferAssetJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
