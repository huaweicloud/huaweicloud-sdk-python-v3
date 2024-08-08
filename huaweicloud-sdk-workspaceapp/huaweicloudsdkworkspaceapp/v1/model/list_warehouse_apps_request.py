# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWarehouseAppsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'verify_status': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'app_category': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'verify_status': 'verify_status',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'app_category': 'app_category'
    }

    def __init__(self, limit=None, offset=None, verify_status=None, app_id=None, app_name=None, app_category=None):
        """ListWarehouseAppsRequest

        The model defined in huaweicloud sdk

        :param limit: 单次查询的大小[1-100]。
        :type limit: int
        :param offset: 查询的偏移量。
        :type offset: int
        :param verify_status: 审核状态。
        :type verify_status: str
        :param app_id: 应用仓库中的应用记录ID。
        :type app_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param app_category: 应用分类： * &#x60;GAME&#x60;-  &#x60;游戏&#x60;。 * &#x60;BUSSINESS_INTELLIGENCE&#x60;- &#x60;商业智能&#x60;。 * &#x60;SECURE_STORAGE&#x60;-  &#x60;安全与存储&#x60;。 * &#x60;MULTIMEDIA_AND_CODING&#x60;- &#x60;多媒体与编解码&#x60;。 * &#x60;PROJECT_MANAGEMENT&#x60;- &#x60;项目管理&#x60;, * &#x60;PRODUCTIVITY_AND_COLLABORATION&#x60;-  &#x60;生产力与协作&#x60;。 * &#x60;WEB_ADN_APPLICATION&#x60;-  &#x60;网页与应用开发&#x60;。 * &#x60;GRAPHIC_DESIGN&#x60;-  &#x60;图形设计&#x60;。 * &#x60;OTHER&#x60;-  &#x60;其它&#x60;。
        :type app_category: str
        """
        
        

        self._limit = None
        self._offset = None
        self._verify_status = None
        self._app_id = None
        self._app_name = None
        self._app_category = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if verify_status is not None:
            self.verify_status = verify_status
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if app_category is not None:
            self.app_category = app_category

    @property
    def limit(self):
        """Gets the limit of this ListWarehouseAppsRequest.

        单次查询的大小[1-100]。

        :return: The limit of this ListWarehouseAppsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWarehouseAppsRequest.

        单次查询的大小[1-100]。

        :param limit: The limit of this ListWarehouseAppsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListWarehouseAppsRequest.

        查询的偏移量。

        :return: The offset of this ListWarehouseAppsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListWarehouseAppsRequest.

        查询的偏移量。

        :param offset: The offset of this ListWarehouseAppsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def verify_status(self):
        """Gets the verify_status of this ListWarehouseAppsRequest.

        审核状态。

        :return: The verify_status of this ListWarehouseAppsRequest.
        :rtype: str
        """
        return self._verify_status

    @verify_status.setter
    def verify_status(self, verify_status):
        """Sets the verify_status of this ListWarehouseAppsRequest.

        审核状态。

        :param verify_status: The verify_status of this ListWarehouseAppsRequest.
        :type verify_status: str
        """
        self._verify_status = verify_status

    @property
    def app_id(self):
        """Gets the app_id of this ListWarehouseAppsRequest.

        应用仓库中的应用记录ID。

        :return: The app_id of this ListWarehouseAppsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListWarehouseAppsRequest.

        应用仓库中的应用记录ID。

        :param app_id: The app_id of this ListWarehouseAppsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this ListWarehouseAppsRequest.

        应用名称。

        :return: The app_name of this ListWarehouseAppsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListWarehouseAppsRequest.

        应用名称。

        :param app_name: The app_name of this ListWarehouseAppsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_category(self):
        """Gets the app_category of this ListWarehouseAppsRequest.

        应用分类： * `GAME`-  `游戏`。 * `BUSSINESS_INTELLIGENCE`- `商业智能`。 * `SECURE_STORAGE`-  `安全与存储`。 * `MULTIMEDIA_AND_CODING`- `多媒体与编解码`。 * `PROJECT_MANAGEMENT`- `项目管理`, * `PRODUCTIVITY_AND_COLLABORATION`-  `生产力与协作`。 * `WEB_ADN_APPLICATION`-  `网页与应用开发`。 * `GRAPHIC_DESIGN`-  `图形设计`。 * `OTHER`-  `其它`。

        :return: The app_category of this ListWarehouseAppsRequest.
        :rtype: str
        """
        return self._app_category

    @app_category.setter
    def app_category(self, app_category):
        """Sets the app_category of this ListWarehouseAppsRequest.

        应用分类： * `GAME`-  `游戏`。 * `BUSSINESS_INTELLIGENCE`- `商业智能`。 * `SECURE_STORAGE`-  `安全与存储`。 * `MULTIMEDIA_AND_CODING`- `多媒体与编解码`。 * `PROJECT_MANAGEMENT`- `项目管理`, * `PRODUCTIVITY_AND_COLLABORATION`-  `生产力与协作`。 * `WEB_ADN_APPLICATION`-  `网页与应用开发`。 * `GRAPHIC_DESIGN`-  `图形设计`。 * `OTHER`-  `其它`。

        :param app_category: The app_category of this ListWarehouseAppsRequest.
        :type app_category: str
        """
        self._app_category = app_category

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
        if not isinstance(other, ListWarehouseAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
