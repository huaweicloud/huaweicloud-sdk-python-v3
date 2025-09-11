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

        :param dashboard_id: **参数描述**： 监控看板id **取值范围** 以db开头，包含22个字母和数字，长度为24个字符 
        :type dashboard_id: str
        :param dashboard_name: **参数解释** 自定义监控看板名称 **取值范围** 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和- 
        :type dashboard_name: str
        :param enterprise_id: **参数解释** 企业项目ID **取值范围** 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID）。 
        :type enterprise_id: str
        :param row_widget_num: **参数解释** 每行展示视图数量 **取值范围** - 0:表示自定义坐标 - 1:代表每行1个视图 - 2:代表每行2个视图 - 3:代表每行3个视图 
        :type row_widget_num: int
        :param is_favorite: **参数解释** 监控看板是否标记收藏 **取值范围** - true: 收藏, - false: 未收藏 
        :type is_favorite: bool
        :param creator_name: **参数解释** 监控看板的创建用户名 **取值范围** 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和- 
        :type creator_name: str
        :param create_time: **参数解释** 监控看板创建时间 **取值范围** 最小值为1111111111111，最大值为9999999999999 
        :type create_time: int
        :param widgets_num: **参数解释** 看板下的视图总数 **取值范围** 最小值为0，最大值为50 
        :type widgets_num: int
        :param namespace: **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 
        :type namespace: str
        :param sub_product: **参数解释** 子产品标识 **取值范围** 长度为[1,128]个字符 
        :type sub_product: str
        :param dashboard_template_id: **参数解释** 监控大盘模板id **取值范围** 以mb开头，包含22个字母和数字，长度为24个字符 
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

        **参数描述**： 监控看板id **取值范围** 以db开头，包含22个字母和数字，长度为24个字符 

        :return: The dashboard_id of this DashBoardInfo.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        r"""Sets the dashboard_id of this DashBoardInfo.

        **参数描述**： 监控看板id **取值范围** 以db开头，包含22个字母和数字，长度为24个字符 

        :param dashboard_id: The dashboard_id of this DashBoardInfo.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def dashboard_name(self):
        r"""Gets the dashboard_name of this DashBoardInfo.

        **参数解释** 自定义监控看板名称 **取值范围** 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和- 

        :return: The dashboard_name of this DashBoardInfo.
        :rtype: str
        """
        return self._dashboard_name

    @dashboard_name.setter
    def dashboard_name(self, dashboard_name):
        r"""Sets the dashboard_name of this DashBoardInfo.

        **参数解释** 自定义监控看板名称 **取值范围** 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和- 

        :param dashboard_name: The dashboard_name of this DashBoardInfo.
        :type dashboard_name: str
        """
        self._dashboard_name = dashboard_name

    @property
    def enterprise_id(self):
        r"""Gets the enterprise_id of this DashBoardInfo.

        **参数解释** 企业项目ID **取值范围** 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID）。 

        :return: The enterprise_id of this DashBoardInfo.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        r"""Sets the enterprise_id of this DashBoardInfo.

        **参数解释** 企业项目ID **取值范围** 只能包含小写字母、数字、“-”、“_”，可以自定义企业项目ID，长度为36个字符。也可以为0（代表默认企业项目ID）。 

        :param enterprise_id: The enterprise_id of this DashBoardInfo.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def row_widget_num(self):
        r"""Gets the row_widget_num of this DashBoardInfo.

        **参数解释** 每行展示视图数量 **取值范围** - 0:表示自定义坐标 - 1:代表每行1个视图 - 2:代表每行2个视图 - 3:代表每行3个视图 

        :return: The row_widget_num of this DashBoardInfo.
        :rtype: int
        """
        return self._row_widget_num

    @row_widget_num.setter
    def row_widget_num(self, row_widget_num):
        r"""Sets the row_widget_num of this DashBoardInfo.

        **参数解释** 每行展示视图数量 **取值范围** - 0:表示自定义坐标 - 1:代表每行1个视图 - 2:代表每行2个视图 - 3:代表每行3个视图 

        :param row_widget_num: The row_widget_num of this DashBoardInfo.
        :type row_widget_num: int
        """
        self._row_widget_num = row_widget_num

    @property
    def is_favorite(self):
        r"""Gets the is_favorite of this DashBoardInfo.

        **参数解释** 监控看板是否标记收藏 **取值范围** - true: 收藏, - false: 未收藏 

        :return: The is_favorite of this DashBoardInfo.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        r"""Sets the is_favorite of this DashBoardInfo.

        **参数解释** 监控看板是否标记收藏 **取值范围** - true: 收藏, - false: 未收藏 

        :param is_favorite: The is_favorite of this DashBoardInfo.
        :type is_favorite: bool
        """
        self._is_favorite = is_favorite

    @property
    def creator_name(self):
        r"""Gets the creator_name of this DashBoardInfo.

        **参数解释** 监控看板的创建用户名 **取值范围** 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和- 

        :return: The creator_name of this DashBoardInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this DashBoardInfo.

        **参数解释** 监控看板的创建用户名 **取值范围** 长度为[1,128]个字符，只允许中文、英文、数字0-9、_和- 

        :param creator_name: The creator_name of this DashBoardInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def create_time(self):
        r"""Gets the create_time of this DashBoardInfo.

        **参数解释** 监控看板创建时间 **取值范围** 最小值为1111111111111，最大值为9999999999999 

        :return: The create_time of this DashBoardInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DashBoardInfo.

        **参数解释** 监控看板创建时间 **取值范围** 最小值为1111111111111，最大值为9999999999999 

        :param create_time: The create_time of this DashBoardInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def widgets_num(self):
        r"""Gets the widgets_num of this DashBoardInfo.

        **参数解释** 看板下的视图总数 **取值范围** 最小值为0，最大值为50 

        :return: The widgets_num of this DashBoardInfo.
        :rtype: int
        """
        return self._widgets_num

    @widgets_num.setter
    def widgets_num(self, widgets_num):
        r"""Sets the widgets_num of this DashBoardInfo.

        **参数解释** 看板下的视图总数 **取值范围** 最小值为0，最大值为50 

        :param widgets_num: The widgets_num of this DashBoardInfo.
        :type widgets_num: int
        """
        self._widgets_num = widgets_num

    @property
    def namespace(self):
        r"""Gets the namespace of this DashBoardInfo.

        **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 

        :return: The namespace of this DashBoardInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this DashBoardInfo.

        **参数解释** 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)” **取值范围** 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 

        :param namespace: The namespace of this DashBoardInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def sub_product(self):
        r"""Gets the sub_product of this DashBoardInfo.

        **参数解释** 子产品标识 **取值范围** 长度为[1,128]个字符 

        :return: The sub_product of this DashBoardInfo.
        :rtype: str
        """
        return self._sub_product

    @sub_product.setter
    def sub_product(self, sub_product):
        r"""Sets the sub_product of this DashBoardInfo.

        **参数解释** 子产品标识 **取值范围** 长度为[1,128]个字符 

        :param sub_product: The sub_product of this DashBoardInfo.
        :type sub_product: str
        """
        self._sub_product = sub_product

    @property
    def dashboard_template_id(self):
        r"""Gets the dashboard_template_id of this DashBoardInfo.

        **参数解释** 监控大盘模板id **取值范围** 以mb开头，包含22个字母和数字，长度为24个字符 

        :return: The dashboard_template_id of this DashBoardInfo.
        :rtype: str
        """
        return self._dashboard_template_id

    @dashboard_template_id.setter
    def dashboard_template_id(self, dashboard_template_id):
        r"""Sets the dashboard_template_id of this DashBoardInfo.

        **参数解释** 监控大盘模板id **取值范围** 以mb开头，包含22个字母和数字，长度为24个字符 

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
