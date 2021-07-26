# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSyncEventsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sync_task_id': 'str',
        'body': 'SyncObjectReq'
    }

    attribute_map = {
        'sync_task_id': 'sync_task_id',
        'body': 'body'
    }

    def __init__(self, sync_task_id=None, body=None):
        """CreateSyncEventsRequest - a model defined in huaweicloud sdk"""
        
        

        self._sync_task_id = None
        self._body = None
        self.discriminator = None

        self.sync_task_id = sync_task_id
        if body is not None:
            self.body = body

    @property
    def sync_task_id(self):
        """Gets the sync_task_id of this CreateSyncEventsRequest.

        同步任务ID

        :return: The sync_task_id of this CreateSyncEventsRequest.
        :rtype: str
        """
        return self._sync_task_id

    @sync_task_id.setter
    def sync_task_id(self, sync_task_id):
        """Sets the sync_task_id of this CreateSyncEventsRequest.

        同步任务ID

        :param sync_task_id: The sync_task_id of this CreateSyncEventsRequest.
        :type: str
        """
        self._sync_task_id = sync_task_id

    @property
    def body(self):
        """Gets the body of this CreateSyncEventsRequest.


        :return: The body of this CreateSyncEventsRequest.
        :rtype: SyncObjectReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateSyncEventsRequest.


        :param body: The body of this CreateSyncEventsRequest.
        :type: SyncObjectReq
        """
        self._body = body

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateSyncEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
