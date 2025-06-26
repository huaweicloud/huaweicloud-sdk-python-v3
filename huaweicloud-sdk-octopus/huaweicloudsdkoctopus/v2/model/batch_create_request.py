# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'algorithm_image': 'str',
        'batch_config': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'algorithm_image': 'algorithm_image',
        'batch_config': 'batch_config'
    }

    def __init__(self, name=None, description=None, algorithm_image=None, batch_config=None):
        r"""BatchCreateRequest

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param description: 文本描述
        :type description: str
        :param algorithm_image: 关联算法镜像，如果任务配置了算法，该字段必填
        :type algorithm_image: str
        :param batch_config: 关联batch配置
        :type batch_config: str
        """
        
        

        self._name = None
        self._description = None
        self._algorithm_image = None
        self._batch_config = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.algorithm_image = algorithm_image
        self.batch_config = batch_config

    @property
    def name(self):
        r"""Gets the name of this BatchCreateRequest.

        名称

        :return: The name of this BatchCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateRequest.

        名称

        :param name: The name of this BatchCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this BatchCreateRequest.

        文本描述

        :return: The description of this BatchCreateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateRequest.

        文本描述

        :param description: The description of this BatchCreateRequest.
        :type description: str
        """
        self._description = description

    @property
    def algorithm_image(self):
        r"""Gets the algorithm_image of this BatchCreateRequest.

        关联算法镜像，如果任务配置了算法，该字段必填

        :return: The algorithm_image of this BatchCreateRequest.
        :rtype: str
        """
        return self._algorithm_image

    @algorithm_image.setter
    def algorithm_image(self, algorithm_image):
        r"""Sets the algorithm_image of this BatchCreateRequest.

        关联算法镜像，如果任务配置了算法，该字段必填

        :param algorithm_image: The algorithm_image of this BatchCreateRequest.
        :type algorithm_image: str
        """
        self._algorithm_image = algorithm_image

    @property
    def batch_config(self):
        r"""Gets the batch_config of this BatchCreateRequest.

        关联batch配置

        :return: The batch_config of this BatchCreateRequest.
        :rtype: str
        """
        return self._batch_config

    @batch_config.setter
    def batch_config(self, batch_config):
        r"""Sets the batch_config of this BatchCreateRequest.

        关联batch配置

        :param batch_config: The batch_config of this BatchCreateRequest.
        :type batch_config: str
        """
        self._batch_config = batch_config

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
        if not isinstance(other, BatchCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
