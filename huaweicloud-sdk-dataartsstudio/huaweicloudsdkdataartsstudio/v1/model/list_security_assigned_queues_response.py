# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityAssignedQueuesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'queue_sources': 'list[QueueSrcAssignEntity]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'queue_sources': 'queue_sources'
    }

    def __init__(self, project_id=None, queue_sources=None):
        r"""ListSecurityAssignedQueuesResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目id。
        :type project_id: str
        :param queue_sources: 队列资源信息。
        :type queue_sources: list[:class:`huaweicloudsdkdataartsstudio.v1.QueueSrcAssignEntity`]
        """
        
        super(ListSecurityAssignedQueuesResponse, self).__init__()

        self._project_id = None
        self._queue_sources = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if queue_sources is not None:
            self.queue_sources = queue_sources

    @property
    def project_id(self):
        r"""Gets the project_id of this ListSecurityAssignedQueuesResponse.

        项目id。

        :return: The project_id of this ListSecurityAssignedQueuesResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListSecurityAssignedQueuesResponse.

        项目id。

        :param project_id: The project_id of this ListSecurityAssignedQueuesResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def queue_sources(self):
        r"""Gets the queue_sources of this ListSecurityAssignedQueuesResponse.

        队列资源信息。

        :return: The queue_sources of this ListSecurityAssignedQueuesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.QueueSrcAssignEntity`]
        """
        return self._queue_sources

    @queue_sources.setter
    def queue_sources(self, queue_sources):
        r"""Sets the queue_sources of this ListSecurityAssignedQueuesResponse.

        队列资源信息。

        :param queue_sources: The queue_sources of this ListSecurityAssignedQueuesResponse.
        :type queue_sources: list[:class:`huaweicloudsdkdataartsstudio.v1.QueueSrcAssignEntity`]
        """
        self._queue_sources = queue_sources

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
        if not isinstance(other, ListSecurityAssignedQueuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
