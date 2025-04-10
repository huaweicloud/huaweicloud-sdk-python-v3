# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'id': 'str',
        'app_name': 'str',
        'region_id': 'str',
        'params': 'list[ResourceQuery]'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'app_name': 'app_name',
        'region_id': 'region_id',
        'params': 'params'
    }

    def __init__(self, type=None, id=None, app_name=None, region_id=None, params=None):
        r"""TargetResource

        The model defined in huaweicloud sdk

        :param type: 资源类型(REGION, APPLICATION)
        :type type: str
        :param id: 资源id
        :type id: str
        :param app_name: 应用名称（层级关系用.隔开）
        :type app_name: str
        :param region_id: region（应用关联region）
        :type region_id: str
        :param params: 动态查询条件
        :type params: list[:class:`huaweicloudsdkcoc.v1.ResourceQuery`]
        """
        
        

        self._type = None
        self._id = None
        self._app_name = None
        self._region_id = None
        self._params = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if app_name is not None:
            self.app_name = app_name
        if region_id is not None:
            self.region_id = region_id
        if params is not None:
            self.params = params

    @property
    def type(self):
        r"""Gets the type of this TargetResource.

        资源类型(REGION, APPLICATION)

        :return: The type of this TargetResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TargetResource.

        资源类型(REGION, APPLICATION)

        :param type: The type of this TargetResource.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this TargetResource.

        资源id

        :return: The id of this TargetResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TargetResource.

        资源id

        :param id: The id of this TargetResource.
        :type id: str
        """
        self._id = id

    @property
    def app_name(self):
        r"""Gets the app_name of this TargetResource.

        应用名称（层级关系用.隔开）

        :return: The app_name of this TargetResource.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this TargetResource.

        应用名称（层级关系用.隔开）

        :param app_name: The app_name of this TargetResource.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def region_id(self):
        r"""Gets the region_id of this TargetResource.

        region（应用关联region）

        :return: The region_id of this TargetResource.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this TargetResource.

        region（应用关联region）

        :param region_id: The region_id of this TargetResource.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def params(self):
        r"""Gets the params of this TargetResource.

        动态查询条件

        :return: The params of this TargetResource.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ResourceQuery`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this TargetResource.

        动态查询条件

        :param params: The params of this TargetResource.
        :type params: list[:class:`huaweicloudsdkcoc.v1.ResourceQuery`]
        """
        self._params = params

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
        if not isinstance(other, TargetResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
