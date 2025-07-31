# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCommonTipsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'CommonList',
        'host_id': 'CommonList',
        'public_ip': 'CommonList',
        'private_ip': 'CommonList',
        'vpc_id': 'CommonList',
        'cluster_id': 'CommonList',
        'host_tags': 'HostTagInfoList'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'vpc_id': 'vpc_id',
        'cluster_id': 'cluster_id',
        'host_tags': 'host_tags'
    }

    def __init__(self, host_name=None, host_id=None, public_ip=None, private_ip=None, vpc_id=None, cluster_id=None, host_tags=None):
        r"""ListCommonTipsResponse

        The model defined in huaweicloud sdk

        :param host_name: 
        :type host_name: :class:`huaweicloudsdkhss.v5.CommonList`
        :param host_id: 
        :type host_id: :class:`huaweicloudsdkhss.v5.CommonList`
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkhss.v5.CommonList`
        :param private_ip: 
        :type private_ip: :class:`huaweicloudsdkhss.v5.CommonList`
        :param vpc_id: 
        :type vpc_id: :class:`huaweicloudsdkhss.v5.CommonList`
        :param cluster_id: 
        :type cluster_id: :class:`huaweicloudsdkhss.v5.CommonList`
        :param host_tags: 
        :type host_tags: :class:`huaweicloudsdkhss.v5.HostTagInfoList`
        """
        
        super(ListCommonTipsResponse, self).__init__()

        self._host_name = None
        self._host_id = None
        self._public_ip = None
        self._private_ip = None
        self._vpc_id = None
        self._cluster_id = None
        self._host_tags = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if host_tags is not None:
            self.host_tags = host_tags

    @property
    def host_name(self):
        r"""Gets the host_name of this ListCommonTipsResponse.

        :return: The host_name of this ListCommonTipsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListCommonTipsResponse.

        :param host_name: The host_name of this ListCommonTipsResponse.
        :type host_name: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListCommonTipsResponse.

        :return: The host_id of this ListCommonTipsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListCommonTipsResponse.

        :param host_id: The host_id of this ListCommonTipsResponse.
        :type host_id: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        self._host_id = host_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListCommonTipsResponse.

        :return: The public_ip of this ListCommonTipsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListCommonTipsResponse.

        :param public_ip: The public_ip of this ListCommonTipsResponse.
        :type public_ip: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListCommonTipsResponse.

        :return: The private_ip of this ListCommonTipsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListCommonTipsResponse.

        :param private_ip: The private_ip of this ListCommonTipsResponse.
        :type private_ip: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        self._private_ip = private_ip

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListCommonTipsResponse.

        :return: The vpc_id of this ListCommonTipsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListCommonTipsResponse.

        :param vpc_id: The vpc_id of this ListCommonTipsResponse.
        :type vpc_id: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        self._vpc_id = vpc_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListCommonTipsResponse.

        :return: The cluster_id of this ListCommonTipsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListCommonTipsResponse.

        :param cluster_id: The cluster_id of this ListCommonTipsResponse.
        :type cluster_id: :class:`huaweicloudsdkhss.v5.CommonList`
        """
        self._cluster_id = cluster_id

    @property
    def host_tags(self):
        r"""Gets the host_tags of this ListCommonTipsResponse.

        :return: The host_tags of this ListCommonTipsResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.HostTagInfoList`
        """
        return self._host_tags

    @host_tags.setter
    def host_tags(self, host_tags):
        r"""Sets the host_tags of this ListCommonTipsResponse.

        :param host_tags: The host_tags of this ListCommonTipsResponse.
        :type host_tags: :class:`huaweicloudsdkhss.v5.HostTagInfoList`
        """
        self._host_tags = host_tags

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
        if not isinstance(other, ListCommonTipsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
