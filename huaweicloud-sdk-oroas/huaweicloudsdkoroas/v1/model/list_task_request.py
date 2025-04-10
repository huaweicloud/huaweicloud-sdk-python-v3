# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_apig_app_code': 'str',
        'service_group': 'str',
        'service_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_apig_app_code': 'X-Apig-AppCode',
        'service_group': 'service_group',
        'service_type': 'service_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_apig_app_code=None, service_group=None, service_type=None, limit=None, offset=None):
        r"""ListTaskRequest

        The model defined in huaweicloud sdk

        :param x_apig_app_code: 用户凭证
        :type x_apig_app_code: str
        :param service_group: 服务类别，针对不同服务类场景，为用户提前填充对应值，用户侧不需单独赋值；当前仅支持 二维切割 2dcut ，便于后续扩展
        :type service_group: str
        :param service_type: 子服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；服装切割固定为 irregular-textile，雕刻机切割固定为 engraving-machine-cutting， 板材切割固定为 regular-plate
        :type service_type: str
        :param limit: 限制量，单次查询总量，必须由数字组成，默认为300，取值范围[1,300]
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]
        :type offset: int
        """
        
        

        self._x_apig_app_code = None
        self._service_group = None
        self._service_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.x_apig_app_code = x_apig_app_code
        self.service_group = service_group
        self.service_type = service_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_apig_app_code(self):
        r"""Gets the x_apig_app_code of this ListTaskRequest.

        用户凭证

        :return: The x_apig_app_code of this ListTaskRequest.
        :rtype: str
        """
        return self._x_apig_app_code

    @x_apig_app_code.setter
    def x_apig_app_code(self, x_apig_app_code):
        r"""Sets the x_apig_app_code of this ListTaskRequest.

        用户凭证

        :param x_apig_app_code: The x_apig_app_code of this ListTaskRequest.
        :type x_apig_app_code: str
        """
        self._x_apig_app_code = x_apig_app_code

    @property
    def service_group(self):
        r"""Gets the service_group of this ListTaskRequest.

        服务类别，针对不同服务类场景，为用户提前填充对应值，用户侧不需单独赋值；当前仅支持 二维切割 2dcut ，便于后续扩展

        :return: The service_group of this ListTaskRequest.
        :rtype: str
        """
        return self._service_group

    @service_group.setter
    def service_group(self, service_group):
        r"""Sets the service_group of this ListTaskRequest.

        服务类别，针对不同服务类场景，为用户提前填充对应值，用户侧不需单独赋值；当前仅支持 二维切割 2dcut ，便于后续扩展

        :param service_group: The service_group of this ListTaskRequest.
        :type service_group: str
        """
        self._service_group = service_group

    @property
    def service_type(self):
        r"""Gets the service_type of this ListTaskRequest.

        子服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；服装切割固定为 irregular-textile，雕刻机切割固定为 engraving-machine-cutting， 板材切割固定为 regular-plate

        :return: The service_type of this ListTaskRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ListTaskRequest.

        子服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；服装切割固定为 irregular-textile，雕刻机切割固定为 engraving-machine-cutting， 板材切割固定为 regular-plate

        :param service_type: The service_type of this ListTaskRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def limit(self):
        r"""Gets the limit of this ListTaskRequest.

        限制量，单次查询总量，必须由数字组成，默认为300，取值范围[1,300]

        :return: The limit of this ListTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTaskRequest.

        限制量，单次查询总量，必须由数字组成，默认为300，取值范围[1,300]

        :param limit: The limit of this ListTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTaskRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :return: The offset of this ListTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTaskRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :param offset: The offset of this ListTaskRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
