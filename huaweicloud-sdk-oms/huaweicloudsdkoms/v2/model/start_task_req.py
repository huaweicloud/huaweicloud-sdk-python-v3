# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'src_ak': 'str',
        'src_sk': 'str',
        'json_auth_file': 'str',
        'src_security_token': 'str',
        'dst_ak': 'str',
        'dst_sk': 'str',
        'dst_security_token': 'str',
        'source_cdn_authentication_key': 'str',
        'migrate_failed_object': 'bool'
    }

    attribute_map = {
        'src_ak': 'src_ak',
        'src_sk': 'src_sk',
        'json_auth_file': 'json_auth_file',
        'src_security_token': 'src_security_token',
        'dst_ak': 'dst_ak',
        'dst_sk': 'dst_sk',
        'dst_security_token': 'dst_security_token',
        'source_cdn_authentication_key': 'source_cdn_authentication_key',
        'migrate_failed_object': 'migrate_failed_object'
    }

    def __init__(self, src_ak=None, src_sk=None, json_auth_file=None, src_security_token=None, dst_ak=None, dst_sk=None, dst_security_token=None, source_cdn_authentication_key=None, migrate_failed_object=None):
        r"""StartTaskReq

        The model defined in huaweicloud sdk

        :param src_ak: 源端节点AK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。
        :type src_ak: str
        :param src_sk: 源端节点SK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。
        :type src_sk: str
        :param json_auth_file: 用于谷歌云Cloud Storage鉴权
        :type json_auth_file: str
        :param src_security_token: 源端节点临时Token
        :type src_security_token: str
        :param dst_ak: 目的端节点AK（最大长度100个字符）。
        :type dst_ak: str
        :param dst_sk: 目的端节点SK（最大长度100个字符）。
        :type dst_sk: str
        :param dst_security_token: 目标端节点临时Token
        :type dst_security_token: str
        :param source_cdn_authentication_key: CDN鉴权秘钥。
        :type source_cdn_authentication_key: str
        :param migrate_failed_object: 迁移类型，标识是否为全量迁移，默认false（全量迁移）。 值为true时表示只重传失败对象。 值为空或者为false时表示全量迁移。
        :type migrate_failed_object: bool
        """
        
        

        self._src_ak = None
        self._src_sk = None
        self._json_auth_file = None
        self._src_security_token = None
        self._dst_ak = None
        self._dst_sk = None
        self._dst_security_token = None
        self._source_cdn_authentication_key = None
        self._migrate_failed_object = None
        self.discriminator = None

        if src_ak is not None:
            self.src_ak = src_ak
        if src_sk is not None:
            self.src_sk = src_sk
        if json_auth_file is not None:
            self.json_auth_file = json_auth_file
        if src_security_token is not None:
            self.src_security_token = src_security_token
        self.dst_ak = dst_ak
        self.dst_sk = dst_sk
        if dst_security_token is not None:
            self.dst_security_token = dst_security_token
        if source_cdn_authentication_key is not None:
            self.source_cdn_authentication_key = source_cdn_authentication_key
        if migrate_failed_object is not None:
            self.migrate_failed_object = migrate_failed_object

    @property
    def src_ak(self):
        r"""Gets the src_ak of this StartTaskReq.

        源端节点AK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。

        :return: The src_ak of this StartTaskReq.
        :rtype: str
        """
        return self._src_ak

    @src_ak.setter
    def src_ak(self, src_ak):
        r"""Sets the src_ak of this StartTaskReq.

        源端节点AK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。

        :param src_ak: The src_ak of this StartTaskReq.
        :type src_ak: str
        """
        self._src_ak = src_ak

    @property
    def src_sk(self):
        r"""Gets the src_sk of this StartTaskReq.

        源端节点SK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。

        :return: The src_sk of this StartTaskReq.
        :rtype: str
        """
        return self._src_sk

    @src_sk.setter
    def src_sk(self, src_sk):
        r"""Sets the src_sk of this StartTaskReq.

        源端节点SK（最大长度100个字符）。URL列表迁移任务不需要填写此参数。

        :param src_sk: The src_sk of this StartTaskReq.
        :type src_sk: str
        """
        self._src_sk = src_sk

    @property
    def json_auth_file(self):
        r"""Gets the json_auth_file of this StartTaskReq.

        用于谷歌云Cloud Storage鉴权

        :return: The json_auth_file of this StartTaskReq.
        :rtype: str
        """
        return self._json_auth_file

    @json_auth_file.setter
    def json_auth_file(self, json_auth_file):
        r"""Sets the json_auth_file of this StartTaskReq.

        用于谷歌云Cloud Storage鉴权

        :param json_auth_file: The json_auth_file of this StartTaskReq.
        :type json_auth_file: str
        """
        self._json_auth_file = json_auth_file

    @property
    def src_security_token(self):
        r"""Gets the src_security_token of this StartTaskReq.

        源端节点临时Token

        :return: The src_security_token of this StartTaskReq.
        :rtype: str
        """
        return self._src_security_token

    @src_security_token.setter
    def src_security_token(self, src_security_token):
        r"""Sets the src_security_token of this StartTaskReq.

        源端节点临时Token

        :param src_security_token: The src_security_token of this StartTaskReq.
        :type src_security_token: str
        """
        self._src_security_token = src_security_token

    @property
    def dst_ak(self):
        r"""Gets the dst_ak of this StartTaskReq.

        目的端节点AK（最大长度100个字符）。

        :return: The dst_ak of this StartTaskReq.
        :rtype: str
        """
        return self._dst_ak

    @dst_ak.setter
    def dst_ak(self, dst_ak):
        r"""Sets the dst_ak of this StartTaskReq.

        目的端节点AK（最大长度100个字符）。

        :param dst_ak: The dst_ak of this StartTaskReq.
        :type dst_ak: str
        """
        self._dst_ak = dst_ak

    @property
    def dst_sk(self):
        r"""Gets the dst_sk of this StartTaskReq.

        目的端节点SK（最大长度100个字符）。

        :return: The dst_sk of this StartTaskReq.
        :rtype: str
        """
        return self._dst_sk

    @dst_sk.setter
    def dst_sk(self, dst_sk):
        r"""Sets the dst_sk of this StartTaskReq.

        目的端节点SK（最大长度100个字符）。

        :param dst_sk: The dst_sk of this StartTaskReq.
        :type dst_sk: str
        """
        self._dst_sk = dst_sk

    @property
    def dst_security_token(self):
        r"""Gets the dst_security_token of this StartTaskReq.

        目标端节点临时Token

        :return: The dst_security_token of this StartTaskReq.
        :rtype: str
        """
        return self._dst_security_token

    @dst_security_token.setter
    def dst_security_token(self, dst_security_token):
        r"""Sets the dst_security_token of this StartTaskReq.

        目标端节点临时Token

        :param dst_security_token: The dst_security_token of this StartTaskReq.
        :type dst_security_token: str
        """
        self._dst_security_token = dst_security_token

    @property
    def source_cdn_authentication_key(self):
        r"""Gets the source_cdn_authentication_key of this StartTaskReq.

        CDN鉴权秘钥。

        :return: The source_cdn_authentication_key of this StartTaskReq.
        :rtype: str
        """
        return self._source_cdn_authentication_key

    @source_cdn_authentication_key.setter
    def source_cdn_authentication_key(self, source_cdn_authentication_key):
        r"""Sets the source_cdn_authentication_key of this StartTaskReq.

        CDN鉴权秘钥。

        :param source_cdn_authentication_key: The source_cdn_authentication_key of this StartTaskReq.
        :type source_cdn_authentication_key: str
        """
        self._source_cdn_authentication_key = source_cdn_authentication_key

    @property
    def migrate_failed_object(self):
        r"""Gets the migrate_failed_object of this StartTaskReq.

        迁移类型，标识是否为全量迁移，默认false（全量迁移）。 值为true时表示只重传失败对象。 值为空或者为false时表示全量迁移。

        :return: The migrate_failed_object of this StartTaskReq.
        :rtype: bool
        """
        return self._migrate_failed_object

    @migrate_failed_object.setter
    def migrate_failed_object(self, migrate_failed_object):
        r"""Sets the migrate_failed_object of this StartTaskReq.

        迁移类型，标识是否为全量迁移，默认false（全量迁移）。 值为true时表示只重传失败对象。 值为空或者为false时表示全量迁移。

        :param migrate_failed_object: The migrate_failed_object of this StartTaskReq.
        :type migrate_failed_object: bool
        """
        self._migrate_failed_object = migrate_failed_object

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
        if not isinstance(other, StartTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
