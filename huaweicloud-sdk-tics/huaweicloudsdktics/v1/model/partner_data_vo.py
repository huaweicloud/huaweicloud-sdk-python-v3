# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartnerDataVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_list': 'list[TicsDatasetColumn]',
        'create_time': 'datetime',
        'data_type': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'partner_domain_name': 'str'
    }

    attribute_map = {
        'column_list': 'column_list',
        'create_time': 'create_time',
        'data_type': 'data_type',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'partner_domain_name': 'partner_domain_name'
    }

    def __init__(self, column_list=None, create_time=None, data_type=None, description=None, id=None, name=None, partner_domain_name=None):
        """PartnerDataVo

        The model defined in huaweicloud sdk

        :param column_list: 字段信息集合
        :type column_list: list[:class:`huaweicloudsdktics.v1.TicsDatasetColumn`]
        :param create_time: 创建时间
        :type create_time: datetime
        :param data_type: 数据类型，DWS.DWS类型数据集，LOCAL_CSV.本地文件类型数集据，MRS.HIVE类型数据集，MYSQL.MySql类型数据集，ORACLE.Oracle类型数据集，RDS.RDS类型数据集
        :type data_type: str
        :param description: 描述
        :type description: str
        :param id: 数据集id
        :type id: str
        :param name: 数据集名称
        :type name: str
        :param partner_domain_name: 参与方租户名称
        :type partner_domain_name: str
        """
        
        

        self._column_list = None
        self._create_time = None
        self._data_type = None
        self._description = None
        self._id = None
        self._name = None
        self._partner_domain_name = None
        self.discriminator = None

        if column_list is not None:
            self.column_list = column_list
        if create_time is not None:
            self.create_time = create_time
        if data_type is not None:
            self.data_type = data_type
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if partner_domain_name is not None:
            self.partner_domain_name = partner_domain_name

    @property
    def column_list(self):
        """Gets the column_list of this PartnerDataVo.

        字段信息集合

        :return: The column_list of this PartnerDataVo.
        :rtype: list[:class:`huaweicloudsdktics.v1.TicsDatasetColumn`]
        """
        return self._column_list

    @column_list.setter
    def column_list(self, column_list):
        """Sets the column_list of this PartnerDataVo.

        字段信息集合

        :param column_list: The column_list of this PartnerDataVo.
        :type column_list: list[:class:`huaweicloudsdktics.v1.TicsDatasetColumn`]
        """
        self._column_list = column_list

    @property
    def create_time(self):
        """Gets the create_time of this PartnerDataVo.

        创建时间

        :return: The create_time of this PartnerDataVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PartnerDataVo.

        创建时间

        :param create_time: The create_time of this PartnerDataVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def data_type(self):
        """Gets the data_type of this PartnerDataVo.

        数据类型，DWS.DWS类型数据集，LOCAL_CSV.本地文件类型数集据，MRS.HIVE类型数据集，MYSQL.MySql类型数据集，ORACLE.Oracle类型数据集，RDS.RDS类型数据集

        :return: The data_type of this PartnerDataVo.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this PartnerDataVo.

        数据类型，DWS.DWS类型数据集，LOCAL_CSV.本地文件类型数集据，MRS.HIVE类型数据集，MYSQL.MySql类型数据集，ORACLE.Oracle类型数据集，RDS.RDS类型数据集

        :param data_type: The data_type of this PartnerDataVo.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def description(self):
        """Gets the description of this PartnerDataVo.

        描述

        :return: The description of this PartnerDataVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PartnerDataVo.

        描述

        :param description: The description of this PartnerDataVo.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this PartnerDataVo.

        数据集id

        :return: The id of this PartnerDataVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartnerDataVo.

        数据集id

        :param id: The id of this PartnerDataVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PartnerDataVo.

        数据集名称

        :return: The name of this PartnerDataVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartnerDataVo.

        数据集名称

        :param name: The name of this PartnerDataVo.
        :type name: str
        """
        self._name = name

    @property
    def partner_domain_name(self):
        """Gets the partner_domain_name of this PartnerDataVo.

        参与方租户名称

        :return: The partner_domain_name of this PartnerDataVo.
        :rtype: str
        """
        return self._partner_domain_name

    @partner_domain_name.setter
    def partner_domain_name(self, partner_domain_name):
        """Sets the partner_domain_name of this PartnerDataVo.

        参与方租户名称

        :param partner_domain_name: The partner_domain_name of this PartnerDataVo.
        :type partner_domain_name: str
        """
        self._partner_domain_name = partner_domain_name

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
        if not isinstance(other, PartnerDataVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
