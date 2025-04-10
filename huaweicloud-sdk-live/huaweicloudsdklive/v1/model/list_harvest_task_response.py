# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHarvestTaskResponse(SdkResponse):

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
        'harvest_tasks': 'list[HarvestTaskCreateSucRsp]'
    }

    attribute_map = {
        'total': 'total',
        'harvest_tasks': 'harvest_tasks'
    }

    def __init__(self, total=None, harvest_tasks=None):
        r"""ListHarvestTaskResponse

        The model defined in huaweicloud sdk

        :param total: 总任务数
        :type total: int
        :param harvest_tasks: 任务信息
        :type harvest_tasks: list[:class:`huaweicloudsdklive.v1.HarvestTaskCreateSucRsp`]
        """
        
        super(ListHarvestTaskResponse, self).__init__()

        self._total = None
        self._harvest_tasks = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if harvest_tasks is not None:
            self.harvest_tasks = harvest_tasks

    @property
    def total(self):
        r"""Gets the total of this ListHarvestTaskResponse.

        总任务数

        :return: The total of this ListHarvestTaskResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListHarvestTaskResponse.

        总任务数

        :param total: The total of this ListHarvestTaskResponse.
        :type total: int
        """
        self._total = total

    @property
    def harvest_tasks(self):
        r"""Gets the harvest_tasks of this ListHarvestTaskResponse.

        任务信息

        :return: The harvest_tasks of this ListHarvestTaskResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.HarvestTaskCreateSucRsp`]
        """
        return self._harvest_tasks

    @harvest_tasks.setter
    def harvest_tasks(self, harvest_tasks):
        r"""Sets the harvest_tasks of this ListHarvestTaskResponse.

        任务信息

        :param harvest_tasks: The harvest_tasks of this ListHarvestTaskResponse.
        :type harvest_tasks: list[:class:`huaweicloudsdklive.v1.HarvestTaskCreateSucRsp`]
        """
        self._harvest_tasks = harvest_tasks

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
        if not isinstance(other, ListHarvestTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
