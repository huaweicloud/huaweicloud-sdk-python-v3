# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOperationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_id': 'str',
        'percentage_complete': 'int',
        'status': 'str',
        'percentage_details': 'list[OrganizationalPercentageDetail]',
        'message': 'str'
    }

    attribute_map = {
        'operation_id': 'operation_id',
        'percentage_complete': 'percentage_complete',
        'status': 'status',
        'percentage_details': 'percentage_details',
        'message': 'message'
    }

    def __init__(self, operation_id=None, percentage_complete=None, status=None, percentage_details=None, message=None):
        """ShowOperationResponse

        The model defined in huaweicloud sdk

        :param operation_id: 操作ID。
        :type operation_id: str
        :param percentage_complete: 完成进度百分比。
        :type percentage_complete: int
        :param status: 状态。
        :type status: str
        :param percentage_details: 创建账号、纳管OU、纳管账号的详细进度信息。
        :type percentage_details: list[:class:`huaweicloudsdkrgc.v1.OrganizationalPercentageDetail`]
        :param message: 错误信息描述。
        :type message: str
        """
        
        super(ShowOperationResponse, self).__init__()

        self._operation_id = None
        self._percentage_complete = None
        self._status = None
        self._percentage_details = None
        self._message = None
        self.discriminator = None

        if operation_id is not None:
            self.operation_id = operation_id
        if percentage_complete is not None:
            self.percentage_complete = percentage_complete
        if status is not None:
            self.status = status
        if percentage_details is not None:
            self.percentage_details = percentage_details
        if message is not None:
            self.message = message

    @property
    def operation_id(self):
        """Gets the operation_id of this ShowOperationResponse.

        操作ID。

        :return: The operation_id of this ShowOperationResponse.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this ShowOperationResponse.

        操作ID。

        :param operation_id: The operation_id of this ShowOperationResponse.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def percentage_complete(self):
        """Gets the percentage_complete of this ShowOperationResponse.

        完成进度百分比。

        :return: The percentage_complete of this ShowOperationResponse.
        :rtype: int
        """
        return self._percentage_complete

    @percentage_complete.setter
    def percentage_complete(self, percentage_complete):
        """Sets the percentage_complete of this ShowOperationResponse.

        完成进度百分比。

        :param percentage_complete: The percentage_complete of this ShowOperationResponse.
        :type percentage_complete: int
        """
        self._percentage_complete = percentage_complete

    @property
    def status(self):
        """Gets the status of this ShowOperationResponse.

        状态。

        :return: The status of this ShowOperationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowOperationResponse.

        状态。

        :param status: The status of this ShowOperationResponse.
        :type status: str
        """
        self._status = status

    @property
    def percentage_details(self):
        """Gets the percentage_details of this ShowOperationResponse.

        创建账号、纳管OU、纳管账号的详细进度信息。

        :return: The percentage_details of this ShowOperationResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.OrganizationalPercentageDetail`]
        """
        return self._percentage_details

    @percentage_details.setter
    def percentage_details(self, percentage_details):
        """Sets the percentage_details of this ShowOperationResponse.

        创建账号、纳管OU、纳管账号的详细进度信息。

        :param percentage_details: The percentage_details of this ShowOperationResponse.
        :type percentage_details: list[:class:`huaweicloudsdkrgc.v1.OrganizationalPercentageDetail`]
        """
        self._percentage_details = percentage_details

    @property
    def message(self):
        """Gets the message of this ShowOperationResponse.

        错误信息描述。

        :return: The message of this ShowOperationResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowOperationResponse.

        错误信息描述。

        :param message: The message of this ShowOperationResponse.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ShowOperationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
