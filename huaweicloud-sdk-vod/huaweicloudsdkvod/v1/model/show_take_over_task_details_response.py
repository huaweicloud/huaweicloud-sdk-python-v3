# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTakeOverTaskDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'task_id': 'str',
        'task_status': 'str',
        'assets': 'list[AssetDetails]'
    }

    attribute_map = {
        'total': 'total',
        'task_id': 'task_id',
        'task_status': 'task_status',
        'assets': 'assets'
    }

    def __init__(self, total=None, task_id=None, task_status=None, assets=None):
        """ShowTakeOverTaskDetailsResponse

        The model defined in huaweicloud sdk

        :param total: 总数。
        :type total: int
        :param task_id: 任务ID。
        :type task_id: str
        :param task_status: 任务状态。
        :type task_status: str
        :param assets: 媒资信息。
        :type assets: list[:class:`huaweicloudsdkvod.v1.AssetDetails`]
        """
        
        super(ShowTakeOverTaskDetailsResponse, self).__init__()

        self._total = None
        self._task_id = None
        self._task_status = None
        self._assets = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if task_id is not None:
            self.task_id = task_id
        if task_status is not None:
            self.task_status = task_status
        if assets is not None:
            self.assets = assets

    @property
    def total(self):
        """Gets the total of this ShowTakeOverTaskDetailsResponse.

        总数。

        :return: The total of this ShowTakeOverTaskDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowTakeOverTaskDetailsResponse.

        总数。

        :param total: The total of this ShowTakeOverTaskDetailsResponse.
        :type total: int
        """
        self._total = total

    @property
    def task_id(self):
        """Gets the task_id of this ShowTakeOverTaskDetailsResponse.

        任务ID。

        :return: The task_id of this ShowTakeOverTaskDetailsResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowTakeOverTaskDetailsResponse.

        任务ID。

        :param task_id: The task_id of this ShowTakeOverTaskDetailsResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_status(self):
        """Gets the task_status of this ShowTakeOverTaskDetailsResponse.

        任务状态。

        :return: The task_status of this ShowTakeOverTaskDetailsResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowTakeOverTaskDetailsResponse.

        任务状态。

        :param task_status: The task_status of this ShowTakeOverTaskDetailsResponse.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def assets(self):
        """Gets the assets of this ShowTakeOverTaskDetailsResponse.

        媒资信息。

        :return: The assets of this ShowTakeOverTaskDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.AssetDetails`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this ShowTakeOverTaskDetailsResponse.

        媒资信息。

        :param assets: The assets of this ShowTakeOverTaskDetailsResponse.
        :type assets: list[:class:`huaweicloudsdkvod.v1.AssetDetails`]
        """
        self._assets = assets

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
        if not isinstance(other, ShowTakeOverTaskDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
