# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterActionsResponse(SdkResponse):

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
        'action_name': 'str',
        'status': 'str',
        'cluster_name': 'str',
        'submit_time': 'str',
        'items': 'list[ActionItemVo]'
    }

    attribute_map = {
        'id': 'id',
        'action_name': 'action_name',
        'status': 'status',
        'cluster_name': 'cluster_name',
        'submit_time': 'submit_time',
        'items': 'items'
    }

    def __init__(self, id=None, action_name=None, status=None, cluster_name=None, submit_time=None, items=None):
        r"""ListClusterActionsResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 任务详情响应体。 **取值范围**： 随机生成的UUID。
        :type id: str
        :param action_name: **参数解释**： 任务名称，同入参字段。 **取值范围**： 不涉及。
        :type action_name: str
        :param status: **参数解释**： 任务状态。 **取值范围**： 不涉及。
        :type status: str
        :param cluster_name: **参数解释**： 集群名称。 **取值范围**： 不涉及。
        :type cluster_name: str
        :param submit_time: **参数解释**： 任务提交时间。 **取值范围**： 不涉及。
        :type submit_time: str
        :param items: **参数解释**： 任务详情子项。 **取值范围**： 不涉及。
        :type items: list[:class:`huaweicloudsdkdws.v2.ActionItemVo`]
        """
        
        super(ListClusterActionsResponse, self).__init__()

        self._id = None
        self._action_name = None
        self._status = None
        self._cluster_name = None
        self._submit_time = None
        self._items = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if action_name is not None:
            self.action_name = action_name
        if status is not None:
            self.status = status
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if submit_time is not None:
            self.submit_time = submit_time
        if items is not None:
            self.items = items

    @property
    def id(self):
        r"""Gets the id of this ListClusterActionsResponse.

        **参数解释**： 任务详情响应体。 **取值范围**： 随机生成的UUID。

        :return: The id of this ListClusterActionsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListClusterActionsResponse.

        **参数解释**： 任务详情响应体。 **取值范围**： 随机生成的UUID。

        :param id: The id of this ListClusterActionsResponse.
        :type id: str
        """
        self._id = id

    @property
    def action_name(self):
        r"""Gets the action_name of this ListClusterActionsResponse.

        **参数解释**： 任务名称，同入参字段。 **取值范围**： 不涉及。

        :return: The action_name of this ListClusterActionsResponse.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this ListClusterActionsResponse.

        **参数解释**： 任务名称，同入参字段。 **取值范围**： 不涉及。

        :param action_name: The action_name of this ListClusterActionsResponse.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def status(self):
        r"""Gets the status of this ListClusterActionsResponse.

        **参数解释**： 任务状态。 **取值范围**： 不涉及。

        :return: The status of this ListClusterActionsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListClusterActionsResponse.

        **参数解释**： 任务状态。 **取值范围**： 不涉及。

        :param status: The status of this ListClusterActionsResponse.
        :type status: str
        """
        self._status = status

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListClusterActionsResponse.

        **参数解释**： 集群名称。 **取值范围**： 不涉及。

        :return: The cluster_name of this ListClusterActionsResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListClusterActionsResponse.

        **参数解释**： 集群名称。 **取值范围**： 不涉及。

        :param cluster_name: The cluster_name of this ListClusterActionsResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def submit_time(self):
        r"""Gets the submit_time of this ListClusterActionsResponse.

        **参数解释**： 任务提交时间。 **取值范围**： 不涉及。

        :return: The submit_time of this ListClusterActionsResponse.
        :rtype: str
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        r"""Sets the submit_time of this ListClusterActionsResponse.

        **参数解释**： 任务提交时间。 **取值范围**： 不涉及。

        :param submit_time: The submit_time of this ListClusterActionsResponse.
        :type submit_time: str
        """
        self._submit_time = submit_time

    @property
    def items(self):
        r"""Gets the items of this ListClusterActionsResponse.

        **参数解释**： 任务详情子项。 **取值范围**： 不涉及。

        :return: The items of this ListClusterActionsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ActionItemVo`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListClusterActionsResponse.

        **参数解释**： 任务详情子项。 **取值范围**： 不涉及。

        :param items: The items of this ListClusterActionsResponse.
        :type items: list[:class:`huaweicloudsdkdws.v2.ActionItemVo`]
        """
        self._items = items

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
        if not isinstance(other, ListClusterActionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
