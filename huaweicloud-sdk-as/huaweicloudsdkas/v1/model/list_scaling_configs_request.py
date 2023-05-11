# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_configuration_name': 'str',
        'image_id': 'str',
        'start_number': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'scaling_configuration_name': 'scaling_configuration_name',
        'image_id': 'image_id',
        'start_number': 'start_number',
        'limit': 'limit'
    }

    def __init__(self, scaling_configuration_name=None, image_id=None, start_number=None, limit=None):
        """ListScalingConfigsRequest

        The model defined in huaweicloud sdk

        :param scaling_configuration_name: 伸缩配置名称。
        :type scaling_configuration_name: str
        :param image_id: 镜像ID，同imageRef。
        :type image_id: str
        :param start_number: 查询的起始行号，默认为0。
        :type start_number: int
        :param limit: 查询的记录条数，默认为20。
        :type limit: int
        """
        
        

        self._scaling_configuration_name = None
        self._image_id = None
        self._start_number = None
        self._limit = None
        self.discriminator = None

        if scaling_configuration_name is not None:
            self.scaling_configuration_name = scaling_configuration_name
        if image_id is not None:
            self.image_id = image_id
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit

    @property
    def scaling_configuration_name(self):
        """Gets the scaling_configuration_name of this ListScalingConfigsRequest.

        伸缩配置名称。

        :return: The scaling_configuration_name of this ListScalingConfigsRequest.
        :rtype: str
        """
        return self._scaling_configuration_name

    @scaling_configuration_name.setter
    def scaling_configuration_name(self, scaling_configuration_name):
        """Sets the scaling_configuration_name of this ListScalingConfigsRequest.

        伸缩配置名称。

        :param scaling_configuration_name: The scaling_configuration_name of this ListScalingConfigsRequest.
        :type scaling_configuration_name: str
        """
        self._scaling_configuration_name = scaling_configuration_name

    @property
    def image_id(self):
        """Gets the image_id of this ListScalingConfigsRequest.

        镜像ID，同imageRef。

        :return: The image_id of this ListScalingConfigsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ListScalingConfigsRequest.

        镜像ID，同imageRef。

        :param image_id: The image_id of this ListScalingConfigsRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingConfigsRequest.

        查询的起始行号，默认为0。

        :return: The start_number of this ListScalingConfigsRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingConfigsRequest.

        查询的起始行号，默认为0。

        :param start_number: The start_number of this ListScalingConfigsRequest.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingConfigsRequest.

        查询的记录条数，默认为20。

        :return: The limit of this ListScalingConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingConfigsRequest.

        查询的记录条数，默认为20。

        :param limit: The limit of this ListScalingConfigsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListScalingConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
