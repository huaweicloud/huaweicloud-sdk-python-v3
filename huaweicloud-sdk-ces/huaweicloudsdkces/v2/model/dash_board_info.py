# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DashBoardInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_id': 'str',
        'dashboard_name': 'str',
        'enterprise_id': 'str',
        'row_widget_num': 'int',
        'is_favorite': 'bool',
        'creator_name': 'str',
        'create_time': 'int',
        'widgets_num': 'int',
        'namespace': 'str',
        'sub_product': 'str',
        'dashboard_template_id': 'str'
    }

    attribute_map = {
        'dashboard_id': 'dashboard_id',
        'dashboard_name': 'dashboard_name',
        'enterprise_id': 'enterprise_id',
        'row_widget_num': 'row_widget_num',
        'is_favorite': 'is_favorite',
        'creator_name': 'creator_name',
        'create_time': 'create_time',
        'widgets_num': 'widgets_num',
        'namespace': 'namespace',
        'sub_product': 'sub_product',
        'dashboard_template_id': 'dashboard_template_id'
    }

    def __init__(self, dashboard_id=None, dashboard_name=None, enterprise_id=None, row_widget_num=None, is_favorite=None, creator_name=None, create_time=None, widgets_num=None, namespace=None, sub_product=None, dashboard_template_id=None):
        r"""DashBoardInfo

        The model defined in huaweicloud sdk

        :param dashboard_id: 监控看板id
        :type dashboard_id: str
        :param dashboard_name: 自定义监控看板名称
        :type dashboard_name: str
        :param enterprise_id: 企业项目Id
        :type enterprise_id: str
        :param row_widget_num: 监控视图展示模式，0表示自定义坐标，1代表每行一个
        :type row_widget_num: int
        :param is_favorite: 监控看板是否标记收藏, true: 收藏, false: 未收藏
        :type is_favorite: bool
        :param creator_name: 监控看板的创建用户名
        :type creator_name: str
        :param create_time: 监控看板创建时间
        :type create_time: int
        :param widgets_num: 看板下的视图总数
        :type widgets_num: int
        :param namespace: 命名空间
        :type namespace: str
        :param sub_product: 子产品标识
        :type sub_product: str
        :param dashboard_template_id: 监控大盘模板id
        :type dashboard_template_id: str
        """
        
        

        self._dashboard_id = None
        self._dashboard_name = None
        self._enterprise_id = None
        self._row_widget_num = None
        self._is_favorite = None
        self._creator_name = None
        self._create_time = None
        self._widgets_num = None
        self._namespace = None
        self._sub_product = None
        self._dashboard_template_id = None
        self.discriminator = None

        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if dashboard_name is not None:
            self.dashboard_name = dashboard_name
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if row_widget_num is not None:
            self.row_widget_num = row_widget_num
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if creator_name is not None:
            self.creator_name = creator_name
        if create_time is not None:
            self.create_time = create_time
        if widgets_num is not None:
            self.widgets_num = widgets_num
        if namespace is not None:
            self.namespace = namespace
        if sub_product is not None:
            self.sub_product = sub_product
        if dashboard_template_id is not None:
            self.dashboard_template_id = dashboard_template_id

    @property
    def dashboard_id(self):
        r"""Gets the dashboard_id of this DashBoardInfo.

        监控看板id

        :return: The dashboard_id of this DashBoardInfo.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        r"""Sets the dashboard_id of this DashBoardInfo.

        监控看板id

        :param dashboard_id: The dashboard_id of this DashBoardInfo.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def dashboard_name(self):
        r"""Gets the dashboard_name of this DashBoardInfo.

        自定义监控看板名称

        :return: The dashboard_name of this DashBoardInfo.
        :rtype: str
        """
        return self._dashboard_name

    @dashboard_name.setter
    def dashboard_name(self, dashboard_name):
        r"""Sets the dashboard_name of this DashBoardInfo.

        自定义监控看板名称

        :param dashboard_name: The dashboard_name of this DashBoardInfo.
        :type dashboard_name: str
        """
        self._dashboard_name = dashboard_name

    @property
    def enterprise_id(self):
        r"""Gets the enterprise_id of this DashBoardInfo.

        企业项目Id

        :return: The enterprise_id of this DashBoardInfo.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        r"""Sets the enterprise_id of this DashBoardInfo.

        企业项目Id

        :param enterprise_id: The enterprise_id of this DashBoardInfo.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def row_widget_num(self):
        r"""Gets the row_widget_num of this DashBoardInfo.

        监控视图展示模式，0表示自定义坐标，1代表每行一个

        :return: The row_widget_num of this DashBoardInfo.
        :rtype: int
        """
        return self._row_widget_num

    @row_widget_num.setter
    def row_widget_num(self, row_widget_num):
        r"""Sets the row_widget_num of this DashBoardInfo.

        监控视图展示模式，0表示自定义坐标，1代表每行一个

        :param row_widget_num: The row_widget_num of this DashBoardInfo.
        :type row_widget_num: int
        """
        self._row_widget_num = row_widget_num

    @property
    def is_favorite(self):
        r"""Gets the is_favorite of this DashBoardInfo.

        监控看板是否标记收藏, true: 收藏, false: 未收藏

        :return: The is_favorite of this DashBoardInfo.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        r"""Sets the is_favorite of this DashBoardInfo.

        监控看板是否标记收藏, true: 收藏, false: 未收藏

        :param is_favorite: The is_favorite of this DashBoardInfo.
        :type is_favorite: bool
        """
        self._is_favorite = is_favorite

    @property
    def creator_name(self):
        r"""Gets the creator_name of this DashBoardInfo.

        监控看板的创建用户名

        :return: The creator_name of this DashBoardInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this DashBoardInfo.

        监控看板的创建用户名

        :param creator_name: The creator_name of this DashBoardInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def create_time(self):
        r"""Gets the create_time of this DashBoardInfo.

        监控看板创建时间

        :return: The create_time of this DashBoardInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DashBoardInfo.

        监控看板创建时间

        :param create_time: The create_time of this DashBoardInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def widgets_num(self):
        r"""Gets the widgets_num of this DashBoardInfo.

        看板下的视图总数

        :return: The widgets_num of this DashBoardInfo.
        :rtype: int
        """
        return self._widgets_num

    @widgets_num.setter
    def widgets_num(self, widgets_num):
        r"""Sets the widgets_num of this DashBoardInfo.

        看板下的视图总数

        :param widgets_num: The widgets_num of this DashBoardInfo.
        :type widgets_num: int
        """
        self._widgets_num = widgets_num

    @property
    def namespace(self):
        r"""Gets the namespace of this DashBoardInfo.

        命名空间

        :return: The namespace of this DashBoardInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this DashBoardInfo.

        命名空间

        :param namespace: The namespace of this DashBoardInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def sub_product(self):
        r"""Gets the sub_product of this DashBoardInfo.

        子产品标识

        :return: The sub_product of this DashBoardInfo.
        :rtype: str
        """
        return self._sub_product

    @sub_product.setter
    def sub_product(self, sub_product):
        r"""Sets the sub_product of this DashBoardInfo.

        子产品标识

        :param sub_product: The sub_product of this DashBoardInfo.
        :type sub_product: str
        """
        self._sub_product = sub_product

    @property
    def dashboard_template_id(self):
        r"""Gets the dashboard_template_id of this DashBoardInfo.

        监控大盘模板id

        :return: The dashboard_template_id of this DashBoardInfo.
        :rtype: str
        """
        return self._dashboard_template_id

    @dashboard_template_id.setter
    def dashboard_template_id(self, dashboard_template_id):
        r"""Sets the dashboard_template_id of this DashBoardInfo.

        监控大盘模板id

        :param dashboard_template_id: The dashboard_template_id of this DashBoardInfo.
        :type dashboard_template_id: str
        """
        self._dashboard_template_id = dashboard_template_id

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
        if not isinstance(other, DashBoardInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
