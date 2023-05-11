# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOtTemplatesReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_id': 'str',
        'name': 'str',
        'description': 'str',
        'datasource_meta': 'object',
        'point_meta': 'object'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'name': 'name',
        'description': 'description',
        'datasource_meta': 'datasource_meta',
        'point_meta': 'point_meta'
    }

    def __init__(self, tpl_id=None, name=None, description=None, datasource_meta=None, point_meta=None):
        """CreateOtTemplatesReqDTO

        The model defined in huaweicloud sdk

        :param tpl_id: 模板id
        :type tpl_id: str
        :param name: 模板名称，允许中、数字、英文大小写、下划线、中划线
        :type name: str
        :param description: 描述
        :type description: str
        :param datasource_meta: 数据源元数据
        :type datasource_meta: object
        :param point_meta: 点位表元数据
        :type point_meta: object
        """
        
        

        self._tpl_id = None
        self._name = None
        self._description = None
        self._datasource_meta = None
        self._point_meta = None
        self.discriminator = None

        self.tpl_id = tpl_id
        self.name = name
        self.description = description
        self.datasource_meta = datasource_meta
        self.point_meta = point_meta

    @property
    def tpl_id(self):
        """Gets the tpl_id of this CreateOtTemplatesReqDTO.

        模板id

        :return: The tpl_id of this CreateOtTemplatesReqDTO.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this CreateOtTemplatesReqDTO.

        模板id

        :param tpl_id: The tpl_id of this CreateOtTemplatesReqDTO.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def name(self):
        """Gets the name of this CreateOtTemplatesReqDTO.

        模板名称，允许中、数字、英文大小写、下划线、中划线

        :return: The name of this CreateOtTemplatesReqDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOtTemplatesReqDTO.

        模板名称，允许中、数字、英文大小写、下划线、中划线

        :param name: The name of this CreateOtTemplatesReqDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateOtTemplatesReqDTO.

        描述

        :return: The description of this CreateOtTemplatesReqDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateOtTemplatesReqDTO.

        描述

        :param description: The description of this CreateOtTemplatesReqDTO.
        :type description: str
        """
        self._description = description

    @property
    def datasource_meta(self):
        """Gets the datasource_meta of this CreateOtTemplatesReqDTO.

        数据源元数据

        :return: The datasource_meta of this CreateOtTemplatesReqDTO.
        :rtype: object
        """
        return self._datasource_meta

    @datasource_meta.setter
    def datasource_meta(self, datasource_meta):
        """Sets the datasource_meta of this CreateOtTemplatesReqDTO.

        数据源元数据

        :param datasource_meta: The datasource_meta of this CreateOtTemplatesReqDTO.
        :type datasource_meta: object
        """
        self._datasource_meta = datasource_meta

    @property
    def point_meta(self):
        """Gets the point_meta of this CreateOtTemplatesReqDTO.

        点位表元数据

        :return: The point_meta of this CreateOtTemplatesReqDTO.
        :rtype: object
        """
        return self._point_meta

    @point_meta.setter
    def point_meta(self, point_meta):
        """Sets the point_meta of this CreateOtTemplatesReqDTO.

        点位表元数据

        :param point_meta: The point_meta of this CreateOtTemplatesReqDTO.
        :type point_meta: object
        """
        self._point_meta = point_meta

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
        if not isinstance(other, CreateOtTemplatesReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
