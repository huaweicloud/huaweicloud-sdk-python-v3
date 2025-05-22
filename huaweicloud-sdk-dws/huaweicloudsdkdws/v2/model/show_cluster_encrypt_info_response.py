# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterEncryptInfoResponse(SdkResponse):

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
        'cluster_id': 'str',
        'master_key_id': 'str',
        'master_key_name': 'str',
        'last_rotate_key_time': 'str',
        'crypt_algorithm': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'cluster_id',
        'master_key_id': 'master_key_id',
        'master_key_name': 'master_key_name',
        'last_rotate_key_time': 'last_rotate_key_time',
        'crypt_algorithm': 'crypt_algorithm'
    }

    def __init__(self, id=None, cluster_id=None, master_key_id=None, master_key_name=None, last_rotate_key_time=None, crypt_algorithm=None):
        r"""ShowClusterEncryptInfoResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 加密ID，仅DWS内部使用。 **取值范围**： 不涉及。
        :type id: str
        :param cluster_id: **参数解释**： 集群ID。 **取值范围**： 不涉及。
        :type cluster_id: str
        :param master_key_id: **参数解释**： KMS密钥ID。 **取值范围**： 不涉及。
        :type master_key_id: str
        :param master_key_name: **参数解释**： KMS密钥名称。 **取值范围**： 不涉及。
        :type master_key_name: str
        :param last_rotate_key_time: **参数解释**： 最后做密钥轮转的时间。 **取值范围**： 不涉及。
        :type last_rotate_key_time: str
        :param crypt_algorithm: **参数解释**： 加密方式。 **取值范围**： 不涉及。
        :type crypt_algorithm: str
        """
        
        super(ShowClusterEncryptInfoResponse, self).__init__()

        self._id = None
        self._cluster_id = None
        self._master_key_id = None
        self._master_key_name = None
        self._last_rotate_key_time = None
        self._crypt_algorithm = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if master_key_id is not None:
            self.master_key_id = master_key_id
        if master_key_name is not None:
            self.master_key_name = master_key_name
        if last_rotate_key_time is not None:
            self.last_rotate_key_time = last_rotate_key_time
        if crypt_algorithm is not None:
            self.crypt_algorithm = crypt_algorithm

    @property
    def id(self):
        r"""Gets the id of this ShowClusterEncryptInfoResponse.

        **参数解释**： 加密ID，仅DWS内部使用。 **取值范围**： 不涉及。

        :return: The id of this ShowClusterEncryptInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowClusterEncryptInfoResponse.

        **参数解释**： 加密ID，仅DWS内部使用。 **取值范围**： 不涉及。

        :param id: The id of this ShowClusterEncryptInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowClusterEncryptInfoResponse.

        **参数解释**： 集群ID。 **取值范围**： 不涉及。

        :return: The cluster_id of this ShowClusterEncryptInfoResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowClusterEncryptInfoResponse.

        **参数解释**： 集群ID。 **取值范围**： 不涉及。

        :param cluster_id: The cluster_id of this ShowClusterEncryptInfoResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def master_key_id(self):
        r"""Gets the master_key_id of this ShowClusterEncryptInfoResponse.

        **参数解释**： KMS密钥ID。 **取值范围**： 不涉及。

        :return: The master_key_id of this ShowClusterEncryptInfoResponse.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        r"""Sets the master_key_id of this ShowClusterEncryptInfoResponse.

        **参数解释**： KMS密钥ID。 **取值范围**： 不涉及。

        :param master_key_id: The master_key_id of this ShowClusterEncryptInfoResponse.
        :type master_key_id: str
        """
        self._master_key_id = master_key_id

    @property
    def master_key_name(self):
        r"""Gets the master_key_name of this ShowClusterEncryptInfoResponse.

        **参数解释**： KMS密钥名称。 **取值范围**： 不涉及。

        :return: The master_key_name of this ShowClusterEncryptInfoResponse.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        r"""Sets the master_key_name of this ShowClusterEncryptInfoResponse.

        **参数解释**： KMS密钥名称。 **取值范围**： 不涉及。

        :param master_key_name: The master_key_name of this ShowClusterEncryptInfoResponse.
        :type master_key_name: str
        """
        self._master_key_name = master_key_name

    @property
    def last_rotate_key_time(self):
        r"""Gets the last_rotate_key_time of this ShowClusterEncryptInfoResponse.

        **参数解释**： 最后做密钥轮转的时间。 **取值范围**： 不涉及。

        :return: The last_rotate_key_time of this ShowClusterEncryptInfoResponse.
        :rtype: str
        """
        return self._last_rotate_key_time

    @last_rotate_key_time.setter
    def last_rotate_key_time(self, last_rotate_key_time):
        r"""Sets the last_rotate_key_time of this ShowClusterEncryptInfoResponse.

        **参数解释**： 最后做密钥轮转的时间。 **取值范围**： 不涉及。

        :param last_rotate_key_time: The last_rotate_key_time of this ShowClusterEncryptInfoResponse.
        :type last_rotate_key_time: str
        """
        self._last_rotate_key_time = last_rotate_key_time

    @property
    def crypt_algorithm(self):
        r"""Gets the crypt_algorithm of this ShowClusterEncryptInfoResponse.

        **参数解释**： 加密方式。 **取值范围**： 不涉及。

        :return: The crypt_algorithm of this ShowClusterEncryptInfoResponse.
        :rtype: str
        """
        return self._crypt_algorithm

    @crypt_algorithm.setter
    def crypt_algorithm(self, crypt_algorithm):
        r"""Sets the crypt_algorithm of this ShowClusterEncryptInfoResponse.

        **参数解释**： 加密方式。 **取值范围**： 不涉及。

        :param crypt_algorithm: The crypt_algorithm of this ShowClusterEncryptInfoResponse.
        :type crypt_algorithm: str
        """
        self._crypt_algorithm = crypt_algorithm

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
        if not isinstance(other, ShowClusterEncryptInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
