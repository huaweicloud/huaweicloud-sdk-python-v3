# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddOtTemplatesResponse(SdkResponse):

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
        'point_meta': 'object',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'name': 'name',
        'description': 'description',
        'datasource_meta': 'datasource_meta',
        'point_meta': 'point_meta',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, tpl_id=None, name=None, description=None, datasource_meta=None, point_meta=None, create_time=None, update_time=None):
        """AddOtTemplatesResponse

        The model defined in huaweicloud sdk

        :param tpl_id: 模板id
        :type tpl_id: str
        :param name: 模板名称
        :type name: str
        :param description: 描述
        :type description: str
        :param datasource_meta: 数据源元数据
        :type datasource_meta: object
        :param point_meta: 点位表元数据
        :type point_meta: object
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        """
        
        super(AddOtTemplatesResponse, self).__init__()

        self._tpl_id = None
        self._name = None
        self._description = None
        self._datasource_meta = None
        self._point_meta = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if tpl_id is not None:
            self.tpl_id = tpl_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if datasource_meta is not None:
            self.datasource_meta = datasource_meta
        if point_meta is not None:
            self.point_meta = point_meta
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def tpl_id(self):
        """Gets the tpl_id of this AddOtTemplatesResponse.

        模板id

        :return: The tpl_id of this AddOtTemplatesResponse.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this AddOtTemplatesResponse.

        模板id

        :param tpl_id: The tpl_id of this AddOtTemplatesResponse.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def name(self):
        """Gets the name of this AddOtTemplatesResponse.

        模板名称

        :return: The name of this AddOtTemplatesResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddOtTemplatesResponse.

        模板名称

        :param name: The name of this AddOtTemplatesResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AddOtTemplatesResponse.

        描述

        :return: The description of this AddOtTemplatesResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddOtTemplatesResponse.

        描述

        :param description: The description of this AddOtTemplatesResponse.
        :type description: str
        """
        self._description = description

    @property
    def datasource_meta(self):
        """Gets the datasource_meta of this AddOtTemplatesResponse.

        数据源元数据

        :return: The datasource_meta of this AddOtTemplatesResponse.
        :rtype: object
        """
        return self._datasource_meta

    @datasource_meta.setter
    def datasource_meta(self, datasource_meta):
        """Sets the datasource_meta of this AddOtTemplatesResponse.

        数据源元数据

        :param datasource_meta: The datasource_meta of this AddOtTemplatesResponse.
        :type datasource_meta: object
        """
        self._datasource_meta = datasource_meta

    @property
    def point_meta(self):
        """Gets the point_meta of this AddOtTemplatesResponse.

        点位表元数据

        :return: The point_meta of this AddOtTemplatesResponse.
        :rtype: object
        """
        return self._point_meta

    @point_meta.setter
    def point_meta(self, point_meta):
        """Sets the point_meta of this AddOtTemplatesResponse.

        点位表元数据

        :param point_meta: The point_meta of this AddOtTemplatesResponse.
        :type point_meta: object
        """
        self._point_meta = point_meta

    @property
    def create_time(self):
        """Gets the create_time of this AddOtTemplatesResponse.

        创建时间

        :return: The create_time of this AddOtTemplatesResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AddOtTemplatesResponse.

        创建时间

        :param create_time: The create_time of this AddOtTemplatesResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AddOtTemplatesResponse.

        最后一次修改时间

        :return: The update_time of this AddOtTemplatesResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AddOtTemplatesResponse.

        最后一次修改时间

        :param update_time: The update_time of this AddOtTemplatesResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, AddOtTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
