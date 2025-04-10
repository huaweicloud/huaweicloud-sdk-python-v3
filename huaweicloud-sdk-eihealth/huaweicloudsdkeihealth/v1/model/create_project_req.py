# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'is_core': 'bool',
        'is_new_bucket': 'bool',
        'bucket_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'tags': 'tags',
        'is_core': 'is_core',
        'is_new_bucket': 'is_new_bucket',
        'bucket_name': 'bucket_name'
    }

    def __init__(self, description=None, name=None, tags=None, is_core=None, is_new_bucket=None, bucket_name=None):
        r"""CreateProjectReq

        The model defined in huaweicloud sdk

        :param description: 项目描述
        :type description: str
        :param name: 项目名称
        :type name: str
        :param tags: 标签
        :type tags: list[str]
        :param is_core: 是否核心项目
        :type is_core: bool
        :param is_new_bucket: 是否新桶, 仅气象支持该字段
        :type is_new_bucket: bool
        :param bucket_name: 桶名, 仅气象支持该字段
        :type bucket_name: str
        """
        
        

        self._description = None
        self._name = None
        self._tags = None
        self._is_core = None
        self._is_new_bucket = None
        self._bucket_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        if tags is not None:
            self.tags = tags
        if is_core is not None:
            self.is_core = is_core
        if is_new_bucket is not None:
            self.is_new_bucket = is_new_bucket
        if bucket_name is not None:
            self.bucket_name = bucket_name

    @property
    def description(self):
        r"""Gets the description of this CreateProjectReq.

        项目描述

        :return: The description of this CreateProjectReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateProjectReq.

        项目描述

        :param description: The description of this CreateProjectReq.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this CreateProjectReq.

        项目名称

        :return: The name of this CreateProjectReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateProjectReq.

        项目名称

        :param name: The name of this CreateProjectReq.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        r"""Gets the tags of this CreateProjectReq.

        标签

        :return: The tags of this CreateProjectReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateProjectReq.

        标签

        :param tags: The tags of this CreateProjectReq.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def is_core(self):
        r"""Gets the is_core of this CreateProjectReq.

        是否核心项目

        :return: The is_core of this CreateProjectReq.
        :rtype: bool
        """
        return self._is_core

    @is_core.setter
    def is_core(self, is_core):
        r"""Sets the is_core of this CreateProjectReq.

        是否核心项目

        :param is_core: The is_core of this CreateProjectReq.
        :type is_core: bool
        """
        self._is_core = is_core

    @property
    def is_new_bucket(self):
        r"""Gets the is_new_bucket of this CreateProjectReq.

        是否新桶, 仅气象支持该字段

        :return: The is_new_bucket of this CreateProjectReq.
        :rtype: bool
        """
        return self._is_new_bucket

    @is_new_bucket.setter
    def is_new_bucket(self, is_new_bucket):
        r"""Sets the is_new_bucket of this CreateProjectReq.

        是否新桶, 仅气象支持该字段

        :param is_new_bucket: The is_new_bucket of this CreateProjectReq.
        :type is_new_bucket: bool
        """
        self._is_new_bucket = is_new_bucket

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CreateProjectReq.

        桶名, 仅气象支持该字段

        :return: The bucket_name of this CreateProjectReq.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CreateProjectReq.

        桶名, 仅气象支持该字段

        :param bucket_name: The bucket_name of this CreateProjectReq.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

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
        if not isinstance(other, CreateProjectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
