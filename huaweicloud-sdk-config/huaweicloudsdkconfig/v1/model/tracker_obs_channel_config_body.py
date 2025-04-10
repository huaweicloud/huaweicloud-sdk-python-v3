# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrackerOBSChannelConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'bucket_prefix': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'bucket_prefix': 'bucket_prefix',
        'region_id': 'region_id'
    }

    def __init__(self, bucket_name=None, bucket_prefix=None, region_id=None):
        r"""TrackerOBSChannelConfigBody

        The model defined in huaweicloud sdk

        :param bucket_name: OBS桶名称
        :type bucket_name: str
        :param bucket_prefix: OBS桶前缀
        :type bucket_prefix: str
        :param region_id: 区域id
        :type region_id: str
        """
        
        

        self._bucket_name = None
        self._bucket_prefix = None
        self._region_id = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if bucket_prefix is not None:
            self.bucket_prefix = bucket_prefix
        self.region_id = region_id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this TrackerOBSChannelConfigBody.

        OBS桶名称

        :return: The bucket_name of this TrackerOBSChannelConfigBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this TrackerOBSChannelConfigBody.

        OBS桶名称

        :param bucket_name: The bucket_name of this TrackerOBSChannelConfigBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def bucket_prefix(self):
        r"""Gets the bucket_prefix of this TrackerOBSChannelConfigBody.

        OBS桶前缀

        :return: The bucket_prefix of this TrackerOBSChannelConfigBody.
        :rtype: str
        """
        return self._bucket_prefix

    @bucket_prefix.setter
    def bucket_prefix(self, bucket_prefix):
        r"""Sets the bucket_prefix of this TrackerOBSChannelConfigBody.

        OBS桶前缀

        :param bucket_prefix: The bucket_prefix of this TrackerOBSChannelConfigBody.
        :type bucket_prefix: str
        """
        self._bucket_prefix = bucket_prefix

    @property
    def region_id(self):
        r"""Gets the region_id of this TrackerOBSChannelConfigBody.

        区域id

        :return: The region_id of this TrackerOBSChannelConfigBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this TrackerOBSChannelConfigBody.

        区域id

        :param region_id: The region_id of this TrackerOBSChannelConfigBody.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, TrackerOBSChannelConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
