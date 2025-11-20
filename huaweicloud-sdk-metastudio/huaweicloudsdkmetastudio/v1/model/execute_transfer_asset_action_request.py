# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTransferAssetActionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'job_id': 'str',
        'action': 'str',
        'body': 'TransJobRejectBody'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'job_id': 'job_id',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, x_app_user_id=None, job_id=None, action=None, body=None):
        r"""ExecuteTransferAssetActionRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param job_id: 任务ID。
        :type job_id: str
        :param action: 控制。 cancel：取消资产转移，仅转移发起方可调用。 accept：接受资产转移，仅转移接受方可调用。 accept_confirm：确认接受资产转移，仅转移接受方可调用，仅需要计费的转移需再次确认。 reject: 拒绝资产转移，仅转移接受方可调用。
        :type action: str
        :param body: Body of the ExecuteTransferAssetActionRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.TransJobRejectBody`
        """
        
        

        self._x_app_user_id = None
        self._job_id = None
        self._action = None
        self._body = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.job_id = job_id
        self.action = action
        if body is not None:
            self.body = body

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ExecuteTransferAssetActionRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ExecuteTransferAssetActionRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ExecuteTransferAssetActionRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ExecuteTransferAssetActionRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ExecuteTransferAssetActionRequest.

        任务ID。

        :return: The job_id of this ExecuteTransferAssetActionRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ExecuteTransferAssetActionRequest.

        任务ID。

        :param job_id: The job_id of this ExecuteTransferAssetActionRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def action(self):
        r"""Gets the action of this ExecuteTransferAssetActionRequest.

        控制。 cancel：取消资产转移，仅转移发起方可调用。 accept：接受资产转移，仅转移接受方可调用。 accept_confirm：确认接受资产转移，仅转移接受方可调用，仅需要计费的转移需再次确认。 reject: 拒绝资产转移，仅转移接受方可调用。

        :return: The action of this ExecuteTransferAssetActionRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExecuteTransferAssetActionRequest.

        控制。 cancel：取消资产转移，仅转移发起方可调用。 accept：接受资产转移，仅转移接受方可调用。 accept_confirm：确认接受资产转移，仅转移接受方可调用，仅需要计费的转移需再次确认。 reject: 拒绝资产转移，仅转移接受方可调用。

        :param action: The action of this ExecuteTransferAssetActionRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        r"""Gets the body of this ExecuteTransferAssetActionRequest.

        :return: The body of this ExecuteTransferAssetActionRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TransJobRejectBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExecuteTransferAssetActionRequest.

        :param body: The body of this ExecuteTransferAssetActionRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.TransJobRejectBody`
        """
        self._body = body

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
        if not isinstance(other, ExecuteTransferAssetActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
