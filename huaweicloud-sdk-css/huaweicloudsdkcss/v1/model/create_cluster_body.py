# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterBody:


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
        'backup_strategy': 'CreateClusterBackupStrategyBody',
        'instance_num': 'int',
        'instance': 'CreateClusterInstanceBody',
        'enterprise_project_id': 'str',
        'tags': 'list[CreateClusterTagsBody]',
        'datastore': 'CreateClusterDatastoreBody',
        'pay_info': 'PayInfoBody'
    }

    attribute_map = {
        'name': 'name',
        'backup_strategy': 'backupStrategy',
        'instance_num': 'instanceNum',
        'instance': 'instance',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'datastore': 'datastore',
        'pay_info': 'payInfo'
    }

    def __init__(self, name=None, backup_strategy=None, instance_num=None, instance=None, enterprise_project_id=None, tags=None, datastore=None, pay_info=None):
        """CreateClusterBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._backup_strategy = None
        self._instance_num = None
        self._instance = None
        self._enterprise_project_id = None
        self._tags = None
        self._datastore = None
        self._pay_info = None
        self.discriminator = None

        self.name = name
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        self.instance_num = instance_num
        self.instance = instance
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        self.datastore = datastore
        if pay_info is not None:
            self.pay_info = pay_info

    @property
    def name(self):
        """Gets the name of this CreateClusterBody.

        集群名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。

        :return: The name of this CreateClusterBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClusterBody.

        集群名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。

        :param name: The name of this CreateClusterBody.
        :type: str
        """
        self._name = name

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateClusterBody.


        :return: The backup_strategy of this CreateClusterBody.
        :rtype: CreateClusterBackupStrategyBody
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateClusterBody.


        :param backup_strategy: The backup_strategy of this CreateClusterBody.
        :type: CreateClusterBackupStrategyBody
        """
        self._backup_strategy = backup_strategy

    @property
    def instance_num(self):
        """Gets the instance_num of this CreateClusterBody.

        集群实例个数，取值范围为1~32。

        :return: The instance_num of this CreateClusterBody.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        """Sets the instance_num of this CreateClusterBody.

        集群实例个数，取值范围为1~32。

        :param instance_num: The instance_num of this CreateClusterBody.
        :type: int
        """
        self._instance_num = instance_num

    @property
    def instance(self):
        """Gets the instance of this CreateClusterBody.


        :return: The instance of this CreateClusterBody.
        :rtype: CreateClusterInstanceBody
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this CreateClusterBody.


        :param instance: The instance of this CreateClusterBody.
        :type: CreateClusterInstanceBody
        """
        self._instance = instance

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateClusterBody.

        企业项目ID。创建集群时，给集群绑定企业项目ID。最大长度36个字符，带\"-\"连字符的UUID格式，或者是字符串\"0\"。\"0\"表示默认企业项目。  说明：关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理服务用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)。

        :return: The enterprise_project_id of this CreateClusterBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateClusterBody.

        企业项目ID。创建集群时，给集群绑定企业项目ID。最大长度36个字符，带\"-\"连字符的UUID格式，或者是字符串\"0\"。\"0\"表示默认企业项目。  说明：关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理服务用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)。

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterBody.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateClusterBody.

        集群标签。 关于标签特性的详细信息，请参见[《标签管理产品介绍》](https://support.huaweicloud.com/productdesc-tms/zh-cn_topic_0071335169.html)。

        :return: The tags of this CreateClusterBody.
        :rtype: list[CreateClusterTagsBody]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateClusterBody.

        集群标签。 关于标签特性的详细信息，请参见[《标签管理产品介绍》](https://support.huaweicloud.com/productdesc-tms/zh-cn_topic_0071335169.html)。

        :param tags: The tags of this CreateClusterBody.
        :type: list[CreateClusterTagsBody]
        """
        self._tags = tags

    @property
    def datastore(self):
        """Gets the datastore of this CreateClusterBody.


        :return: The datastore of this CreateClusterBody.
        :rtype: CreateClusterDatastoreBody
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateClusterBody.


        :param datastore: The datastore of this CreateClusterBody.
        :type: CreateClusterDatastoreBody
        """
        self._datastore = datastore

    @property
    def pay_info(self):
        """Gets the pay_info of this CreateClusterBody.


        :return: The pay_info of this CreateClusterBody.
        :rtype: PayInfoBody
        """
        return self._pay_info

    @pay_info.setter
    def pay_info(self, pay_info):
        """Sets the pay_info of this CreateClusterBody.


        :param pay_info: The pay_info of this CreateClusterBody.
        :type: PayInfoBody
        """
        self._pay_info = pay_info

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
        if not isinstance(other, CreateClusterBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
