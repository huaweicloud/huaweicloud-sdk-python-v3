# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInstanceRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'TaskInstanceStatusRsp',
        'metadata': 'TaskInstanceMetadataRsp',
        'spec': 'TaskInstanceSpecRsp'
    }

    attribute_map = {
        'status': 'status',
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, status=None, metadata=None, spec=None):
        """TaskInstanceRsp

        The model defined in huaweicloud sdk

        :param status: 
        :type status: :class:`huaweicloudsdkeihealth.v1.TaskInstanceStatusRsp`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkeihealth.v1.TaskInstanceMetadataRsp`
        :param spec: 
        :type spec: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecRsp`
        """
        
        

        self._status = None
        self._metadata = None
        self._spec = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec

    @property
    def status(self):
        """Gets the status of this TaskInstanceRsp.

        :return: The status of this TaskInstanceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskInstanceStatusRsp`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskInstanceRsp.

        :param status: The status of this TaskInstanceRsp.
        :type status: :class:`huaweicloudsdkeihealth.v1.TaskInstanceStatusRsp`
        """
        self._status = status

    @property
    def metadata(self):
        """Gets the metadata of this TaskInstanceRsp.

        :return: The metadata of this TaskInstanceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskInstanceMetadataRsp`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TaskInstanceRsp.

        :param metadata: The metadata of this TaskInstanceRsp.
        :type metadata: :class:`huaweicloudsdkeihealth.v1.TaskInstanceMetadataRsp`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this TaskInstanceRsp.

        :return: The spec of this TaskInstanceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecRsp`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this TaskInstanceRsp.

        :param spec: The spec of this TaskInstanceRsp.
        :type spec: :class:`huaweicloudsdkeihealth.v1.TaskInstanceSpecRsp`
        """
        self._spec = spec

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
        if not isinstance(other, TaskInstanceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
