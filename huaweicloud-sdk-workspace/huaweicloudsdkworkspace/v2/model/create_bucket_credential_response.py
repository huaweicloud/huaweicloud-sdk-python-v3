# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBucketCredentialResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_end_point': 'str',
        'bucket_name': 'str',
        'object_path': 'str',
        'policy': 'ObsPolicy',
        'credential': 'ObsCredential'
    }

    attribute_map = {
        'server_end_point': 'server_end_point',
        'bucket_name': 'bucket_name',
        'object_path': 'object_path',
        'policy': 'policy',
        'credential': 'credential'
    }

    def __init__(self, server_end_point=None, bucket_name=None, object_path=None, policy=None, credential=None):
        r"""CreateBucketCredentialResponse

        The model defined in huaweicloud sdk

        :param server_end_point: 访问的服务终端节点。
        :type server_end_point: str
        :param bucket_name: 存放的桶名称。
        :type bucket_name: str
        :param object_path: OBS对象路径。 注: path是对象在obs中的完整路径。 例如桶存在如下目录结构的数据。   Bucket:     ├─dir1     | ├─object1.txt     | └─object2.txt     └─object3.txt Object1的path: dir1/object1.txt Object2的path: dir1/object2.txt Object3的path: object3.txt
        :type object_path: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkworkspace.v2.ObsPolicy`
        :param credential: 
        :type credential: :class:`huaweicloudsdkworkspace.v2.ObsCredential`
        """
        
        super(CreateBucketCredentialResponse, self).__init__()

        self._server_end_point = None
        self._bucket_name = None
        self._object_path = None
        self._policy = None
        self._credential = None
        self.discriminator = None

        if server_end_point is not None:
            self.server_end_point = server_end_point
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if object_path is not None:
            self.object_path = object_path
        if policy is not None:
            self.policy = policy
        if credential is not None:
            self.credential = credential

    @property
    def server_end_point(self):
        r"""Gets the server_end_point of this CreateBucketCredentialResponse.

        访问的服务终端节点。

        :return: The server_end_point of this CreateBucketCredentialResponse.
        :rtype: str
        """
        return self._server_end_point

    @server_end_point.setter
    def server_end_point(self, server_end_point):
        r"""Sets the server_end_point of this CreateBucketCredentialResponse.

        访问的服务终端节点。

        :param server_end_point: The server_end_point of this CreateBucketCredentialResponse.
        :type server_end_point: str
        """
        self._server_end_point = server_end_point

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CreateBucketCredentialResponse.

        存放的桶名称。

        :return: The bucket_name of this CreateBucketCredentialResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CreateBucketCredentialResponse.

        存放的桶名称。

        :param bucket_name: The bucket_name of this CreateBucketCredentialResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def object_path(self):
        r"""Gets the object_path of this CreateBucketCredentialResponse.

        OBS对象路径。 注: path是对象在obs中的完整路径。 例如桶存在如下目录结构的数据。   Bucket:     ├─dir1     | ├─object1.txt     | └─object2.txt     └─object3.txt Object1的path: dir1/object1.txt Object2的path: dir1/object2.txt Object3的path: object3.txt

        :return: The object_path of this CreateBucketCredentialResponse.
        :rtype: str
        """
        return self._object_path

    @object_path.setter
    def object_path(self, object_path):
        r"""Sets the object_path of this CreateBucketCredentialResponse.

        OBS对象路径。 注: path是对象在obs中的完整路径。 例如桶存在如下目录结构的数据。   Bucket:     ├─dir1     | ├─object1.txt     | └─object2.txt     └─object3.txt Object1的path: dir1/object1.txt Object2的path: dir1/object2.txt Object3的path: object3.txt

        :param object_path: The object_path of this CreateBucketCredentialResponse.
        :type object_path: str
        """
        self._object_path = object_path

    @property
    def policy(self):
        r"""Gets the policy of this CreateBucketCredentialResponse.

        :return: The policy of this CreateBucketCredentialResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ObsPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this CreateBucketCredentialResponse.

        :param policy: The policy of this CreateBucketCredentialResponse.
        :type policy: :class:`huaweicloudsdkworkspace.v2.ObsPolicy`
        """
        self._policy = policy

    @property
    def credential(self):
        r"""Gets the credential of this CreateBucketCredentialResponse.

        :return: The credential of this CreateBucketCredentialResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ObsCredential`
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        r"""Sets the credential of this CreateBucketCredentialResponse.

        :param credential: The credential of this CreateBucketCredentialResponse.
        :type credential: :class:`huaweicloudsdkworkspace.v2.ObsCredential`
        """
        self._credential = credential

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
        if not isinstance(other, CreateBucketCredentialResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
