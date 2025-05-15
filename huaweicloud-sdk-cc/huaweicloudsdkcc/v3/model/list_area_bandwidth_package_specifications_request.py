# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAreaBandwidthPackageSpecificationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_area_id': 'list[str]',
        'remote_area_id': 'list[str]'
    }

    attribute_map = {
        'local_area_id': 'local_area_id',
        'remote_area_id': 'remote_area_id'
    }

    def __init__(self, local_area_id=None, remote_area_id=None):
        r"""ListAreaBandwidthPackageSpecificationsRequest

        The model defined in huaweicloud sdk

        :param local_area_id: 根据本端大区ID过滤带宽包资源规格列表
        :type local_area_id: list[str]
        :param remote_area_id: 根据对端大区ID过滤带宽包资源规格列表
        :type remote_area_id: list[str]
        """
        
        

        self._local_area_id = None
        self._remote_area_id = None
        self.discriminator = None

        if local_area_id is not None:
            self.local_area_id = local_area_id
        if remote_area_id is not None:
            self.remote_area_id = remote_area_id

    @property
    def local_area_id(self):
        r"""Gets the local_area_id of this ListAreaBandwidthPackageSpecificationsRequest.

        根据本端大区ID过滤带宽包资源规格列表

        :return: The local_area_id of this ListAreaBandwidthPackageSpecificationsRequest.
        :rtype: list[str]
        """
        return self._local_area_id

    @local_area_id.setter
    def local_area_id(self, local_area_id):
        r"""Sets the local_area_id of this ListAreaBandwidthPackageSpecificationsRequest.

        根据本端大区ID过滤带宽包资源规格列表

        :param local_area_id: The local_area_id of this ListAreaBandwidthPackageSpecificationsRequest.
        :type local_area_id: list[str]
        """
        self._local_area_id = local_area_id

    @property
    def remote_area_id(self):
        r"""Gets the remote_area_id of this ListAreaBandwidthPackageSpecificationsRequest.

        根据对端大区ID过滤带宽包资源规格列表

        :return: The remote_area_id of this ListAreaBandwidthPackageSpecificationsRequest.
        :rtype: list[str]
        """
        return self._remote_area_id

    @remote_area_id.setter
    def remote_area_id(self, remote_area_id):
        r"""Sets the remote_area_id of this ListAreaBandwidthPackageSpecificationsRequest.

        根据对端大区ID过滤带宽包资源规格列表

        :param remote_area_id: The remote_area_id of this ListAreaBandwidthPackageSpecificationsRequest.
        :type remote_area_id: list[str]
        """
        self._remote_area_id = remote_area_id

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
        if not isinstance(other, ListAreaBandwidthPackageSpecificationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
