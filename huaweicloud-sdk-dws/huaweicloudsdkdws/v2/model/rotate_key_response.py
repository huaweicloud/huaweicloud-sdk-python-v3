# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RotateKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_key_name': 'str',
        'cluster_id': 'str',
        'rotate_key_time': 'str'
    }

    attribute_map = {
        'master_key_name': 'master_key_name',
        'cluster_id': 'cluster_id',
        'rotate_key_time': 'rotate_key_time'
    }

    def __init__(self, master_key_name=None, cluster_id=None, rotate_key_time=None):
        r"""RotateKeyResponse

        The model defined in huaweicloud sdk

        :param master_key_name: **参数解释**： KMS密钥名称 **取值范围**： 不涉及。
        :type master_key_name: str
        :param cluster_id: **参数解释**： 集群ID。 **取值范围**： 不涉及。
        :type cluster_id: str
        :param rotate_key_time: **参数解释**： 轮转时间。 **取值范围**： 不涉及。
        :type rotate_key_time: str
        """
        
        super(RotateKeyResponse, self).__init__()

        self._master_key_name = None
        self._cluster_id = None
        self._rotate_key_time = None
        self.discriminator = None

        if master_key_name is not None:
            self.master_key_name = master_key_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if rotate_key_time is not None:
            self.rotate_key_time = rotate_key_time

    @property
    def master_key_name(self):
        r"""Gets the master_key_name of this RotateKeyResponse.

        **参数解释**： KMS密钥名称 **取值范围**： 不涉及。

        :return: The master_key_name of this RotateKeyResponse.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        r"""Sets the master_key_name of this RotateKeyResponse.

        **参数解释**： KMS密钥名称 **取值范围**： 不涉及。

        :param master_key_name: The master_key_name of this RotateKeyResponse.
        :type master_key_name: str
        """
        self._master_key_name = master_key_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this RotateKeyResponse.

        **参数解释**： 集群ID。 **取值范围**： 不涉及。

        :return: The cluster_id of this RotateKeyResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this RotateKeyResponse.

        **参数解释**： 集群ID。 **取值范围**： 不涉及。

        :param cluster_id: The cluster_id of this RotateKeyResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def rotate_key_time(self):
        r"""Gets the rotate_key_time of this RotateKeyResponse.

        **参数解释**： 轮转时间。 **取值范围**： 不涉及。

        :return: The rotate_key_time of this RotateKeyResponse.
        :rtype: str
        """
        return self._rotate_key_time

    @rotate_key_time.setter
    def rotate_key_time(self, rotate_key_time):
        r"""Sets the rotate_key_time of this RotateKeyResponse.

        **参数解释**： 轮转时间。 **取值范围**： 不涉及。

        :param rotate_key_time: The rotate_key_time of this RotateKeyResponse.
        :type rotate_key_time: str
        """
        self._rotate_key_time = rotate_key_time

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
        if not isinstance(other, RotateKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
